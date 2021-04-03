import Vue from "vue";
import Vuex from "vuex";
import xmlData from "!!raw-loader!@/assets/template.xsd";
import parser from "fast-xml-parser";
import axios from "axios";

import {
  RootState
  // ,
  // XmlComplexTypes,
  // XmlComplexType,
  // XmlElement
} from "@/types";
=======
>>>>>>> ca50a1b (Sorting Frontend Files to its folder)

Vue.use(Vuex);

export default new Vuex.Store<RootState>({
  state: { complexTypeData: jsonObj.schema.complexType ,xmlFile:""},
  mutations: {
    addComplexTypeData(state, data) {
      state.complexTypeData.push(data);
    },
    addXmlFile(state,data){
      state.xmlFile=data;
    }
  },
  actions: {
    addXmlFile({commit,state},data){
      commit("addXmlFile",data);
      axios({
        method:'post',
        url:"http://localhost:5000/api/xmlFile",
        data:data,
        headers: { "Content-Type": "text/plain" },
      });
    }
  },
  modules: {},
  getters: {
    type: state => (type: string) => {
      return state.complexTypeData.find(
        x => x.name === type.replace(/^sample:/, "")
      );
    }
  }
});
