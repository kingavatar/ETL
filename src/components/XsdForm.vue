<template>
  <b-container fluid class="main-form" style="padding:0px;">
    <b-row>
      <b-col>
        <b-button>Back</b-button>
      </b-col>
      <b-col>
        <b-button @click="getXML">Run</b-button>
      </b-col>
    </b-row>
    <XmlElementForm
      class="shadow"
      v-bind:key="getJson.schema.element.name"
      :name="getJson.schema.element.name"
      :type="getJson.schema.element.type"
      parentType=""
      ref="xmlForm"
      idx=""
    />
  </b-container>
</template>

<script>
import parser from "fast-xml-parser";
import { mapState } from "vuex";
import XmlElementForm from "@/components/XmlElementForm.vue";

import Vue from "vue";
export default Vue.extend({
  name: "XsdForm",
  props: { xsdFile: String },
  data() {
    return {};
  },
  components: { XmlElementForm },
  methods: {
    generateXml(ref, xmlFile) {
      if ("elems" in ref.$refs) {
        xmlFile.push("<" + ref.$props.name + ">");
        ref.$refs.elems.forEach(value => {
          this.generateXml(value, xmlFile);
        });
        xmlFile.push("</" + ref.$props.name + ">");
      } else if ("formInput" in ref.$refs) {
        xmlFile.push("<" + ref.$props.name + ">");
        xmlFile.push(ref.formValue);
        xmlFile.push("</" + ref.$props.name + ">");
      }
    },
    getXML() {
      const xmlFile = [];
      this.generateXml(this.$refs.xmlForm, xmlFile);
      const xmlString = xmlFile.join("\n");
      console.log(xmlString);
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
