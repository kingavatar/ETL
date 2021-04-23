<template>
  <b-container fluid class="main-form" style="padding:0px;" v-if="show">
    <b-form @submit="getXML">
      <b-row class="my-4">
        <b-col>
          <b-button>Back</b-button>
        </b-col>
        <b-col>
          <b-button @click="makeToast('info')">Ping Server!</b-button>
        </b-col>
        <b-col>
          <b-button type="submit">Run</b-button>
        </b-col>
      </b-row>
      <XmlElementForm
        class="shadow"
        v-bind:key="getJson.schema.element.name"
        :name="getJson.schema.element.name"
        :type="getJson.schema.element.type"
        parentType=""
        ref="xmlForm"
        idx="0"
      />
    </b-form>
  </b-container>
</template>

<script>
import parser from "fast-xml-parser";
import { mapState } from "vuex";
import XmlElementForm from "@/components/XmlElementForm.vue";
import axios from "axios";
import Vue from "vue";
export default Vue.extend({
  name: "XsdForm",
  props: { xsdFile: String },
  data() {
    return {
      show: true
    };
  },
  components: { XmlElementForm },
  sockets: {
    toast: function(data) {
      this.$bvToast.toast(data.msg, {
        title: `Message ${data.type}`,
        variant: data.type,
        solid: true
      });
    }
  },
  methods: {
    generateXml(ref, xmlFile) {
      if ("elems" in ref.$refs) {
        xmlFile.push("<" + ref.$props.name + ">");
        // console.log(ref.$refs.elems);
        ref.$refs.elems.forEach(value => {
          this.generateXml(value, xmlFile);
        });
        xmlFile.push("</" + ref.$props.name + ">");
      } else if ("formInput" in ref.$refs) {
        xmlFile.push(
          "<" +
            ref.$props.name +
            ">" +
            ref.formValue +
            "</" +
            ref.$props.name +
            ">"
        );
        // xmlFile.push(ref.formValue);
        // xmlFile.push("</" + ref.$props.name + ">");
      }
    },
    getXML(event) {
      event.preventDefault();
      const xmlFile = ['<?xml version="1.0" encoding="utf-8" ?>'];
      this.generateXml(this.$refs.xmlForm, xmlFile);
      xmlFile[1] =
        xmlFile[1].slice(0, -1) +
        ' xmlns ="' +
        this.getJson.schema.targetNamespace +
        '" >';
      const xmlString = xmlFile.join("\n");
      this.$store.dispatch("addXmlFile", xmlString);
    },
    onReset(event) {
      event.preventDefault();
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    makeToast() {
      axios("http://localhost:5000/api/toast");
    }
  },
  computed: {
    options() {
      return {
        attributeNamePrefix: "",
        ignoreAttributes: false,
        ignoreNameSpace: false,
        allowBooleanAttributes: true,
        parseNodeValue: true,
        parseAttributeValue: true,
        trimValues: true,
        parseTrueNumberOnly: true,
        arrayMode: false //"strict"
      };
    },
    getJson() {
      // console.log(this.xsdFile);
      const result = parser.validate(this.xsdFile);
      if (result !== true) console.log(result.err);
      const jsonObj = parser.parse(this.xsdFile, this.options);
      // console.log(jsonObj);
      return jsonObj;
    },
    ...mapState(["complexTypeData"])
  },
  mounted() {
    // console.log(this.xsdFile);
    // const result = parser.validate(this.xsdFile);
    // if (result !== true) console.log(result.err);
    // this.jsonObj = parser.parse(this.xsdFile, this.options);
    // console.log(this.jsonObj);
  }
});
</script>

<style lang="scss" scoped>
.main-form {
  width: 90%;
}
</style>
