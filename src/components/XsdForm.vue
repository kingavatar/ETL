<template>
  <b-container fluid class="main-form shadow" style="padding:0px;">
    <XmlElementForm
      :name="getJson.schema.element.name"
      :type="getJson.schema.element.type"
      parentType=""
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
  components: { XmlElementForm },
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
  },
  data() {
    return {
      // jsonObj:{},
    };
  }
});
</script>

<style lang="scss" scoped>
.main-form {
  width: 90%;
}
</style>
