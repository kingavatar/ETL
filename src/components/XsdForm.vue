<template>
  <div>
    <XmlElementForm :name="getJson.schema.element.name" :type="getJson.schema.element.type"/>
  </div>
</template>

<script>
import parser from "fast-xml-parser";
import { mapState } from 'vuex'
import XmlElementForm from "@/components/XmlElementForm.vue";

import Vue from "vue";
export default Vue.extend({
  name: "XsdForm",
  props: { xsdFile: String },
  components: { XmlElementForm },
  computed: {
    options() {
      return {
        attributeNamePrefix : "",
        ignoreAttributes: false,
        ignoreNameSpace: false,
        allowBooleanAttributes: true,
        parseNodeValue: true,
        parseAttributeValue: true,
        trimValues: true,
        parseTrueNumberOnly: true,
        arrayMode: false, //"strict"
      };
    },
    getJson(){
    // console.log(this.xsdFile);

      const result = parser.validate(this.xsdFile);
    if (result !== true) console.log(result.err);
    const jsonObj = parser.parse(this.xsdFile, this.options);
    console.log(jsonObj);
      return jsonObj;
    },
    ...mapState([
      'complexTypeData'
    ])
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
      form: {
        root: {
          name: "ETL",
          id: "0",
          type: "sample:ETLType",
          elements: [
            {
              name: "sourceDetails",
              id: "1",
              minOccurs: 1,
              maxOccurs: "unbounded",
              type: "sample:sourceDetailsType",
              elements: [
                {
                  name: "sourceinfo",
                  id: "2",
                  type: "sample:sourceinfoType",
                  choice: {
                    id: "3",
                    elements: [
                      {
                        name: "SQL",
                        id: "4",
                        type: "sample:sqlProtocolType",
                        elements: [
                          { name: "name", id: "5", type: "string" },
                          { name: "driver", id: "6", type: "string" },
                          { name: "username", id: "7", type: "string" },
                          { name: "password", id: "8", type: "string" }
                        ]
                      },
                      {
                        name: "FTP",
                        id: "9",
                        type: "sample:ftpProtocolType",
                        username: { id: "10", type: "string" },
                        password: { id: "11", type: "string" },
                        ipaddress: { id: "12", type: "string" }
                      }
                    ]
                  }
                }
              ]
            }
          ]
        }
      }
    };
  },
});
</script>

<style lang="scss" scoped></style>
