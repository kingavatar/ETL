import Vue from "vue";
import Vuex from "vuex";
import xmlData from "!!raw-loader!@/assets/template.xsd";
import parser from "fast-xml-parser";
<<<<<<< HEAD
import axios from "axios";

=======
>>>>>>> affadef (Sorting Files into folders)
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

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {}
});
