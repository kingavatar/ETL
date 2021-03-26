import Vue from "vue";
import Vuex from "vuex";
import xmlData from "!!raw-loader!@/assets/template.xsd";
import parser from "fast-xml-parser";
import {
  RootState
  // ,
  // XmlComplexTypes,
  // XmlComplexType,
  // XmlElement
} from "@/types";

Vue.use(Vuex);
const options = {
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
const jsonObj = parser.parse(xmlData, options);

export default new Vuex.Store<RootState>({
  state: { complexTypeData: jsonObj.schema.complexType },
  mutations: {
    addComplexTypeData(state, data) {
      state.complexTypeData.push(data);
    }
  },
  actions: {},
  modules: {},
  getters: {
    type: state => (type: string) => {
      return state.complexTypeData.find(
        x => x.name === type.replace(/^sample:/, "")
      );
    }
  }
});
