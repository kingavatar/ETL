(function(e){function t(t){for(var r,s,i=t[0],l=t[1],c=t[2],m=0,u=[];m<i.length;m++)s=i[m],Object.prototype.hasOwnProperty.call(a,s)&&a[s]&&u.push(a[s][0]),a[s]=0;for(r in l)Object.prototype.hasOwnProperty.call(l,r)&&(e[r]=l[r]);p&&p(t);while(u.length)u.shift()();return o.push.apply(o,c||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],r=!0,s=1;s<n.length;s++){var l=n[s];0!==a[l]&&(r=!1)}r&&(o.splice(t--,1),e=i(i.s=n[0]))}return e}var r={},a={app:0},o=[];function s(e){return i.p+"js/"+({about:"about"}[e]||e)+"."+{about:"39d35ee4"}[e]+".js"}function i(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,i),n.l=!0,n.exports}i.e=function(e){var t=[],n=a[e];if(0!==n)if(n)t.push(n[2]);else{var r=new Promise((function(t,r){n=a[e]=[t,r]}));t.push(n[2]=r);var o,l=document.createElement("script");l.charset="utf-8",l.timeout=120,i.nc&&l.setAttribute("nonce",i.nc),l.src=s(e);var c=new Error;o=function(t){l.onerror=l.onload=null,clearTimeout(m);var n=a[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;c.message="Loading chunk "+e+" failed.\n("+r+": "+o+")",c.name="ChunkLoadError",c.type=r,c.request=o,n[1](c)}a[e]=void 0}};var m=setTimeout((function(){o({type:"timeout",target:l})}),12e4);l.onerror=l.onload=o,document.head.appendChild(l)}return Promise.all(t)},i.m=e,i.c=r,i.d=function(e,t,n){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(i.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)i.d(n,r,function(t){return e[t]}.bind(null,r));return n},i.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/",i.oe=function(e){throw console.error(e),e};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],c=l.push.bind(l);l.push=t,l=l.slice();for(var m=0;m<l.length;m++)t(l[m]);var p=c;o.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("cd49")},2748:function(e,t,n){"use strict";n("e386")},"300d":function(e,t,n){"use strict";n("4882")},4882:function(e,t,n){},"5c0b":function(e,t,n){"use strict";n("9c0c")},"9c0c":function(e,t,n){},cd49:function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d"),n("e792"),n("0cdd");var r=n("2b0e"),a=n("5f5b");n("ab8b"),n("2dd8");r["default"].use(a["a"]);var o=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("div",{attrs:{id:"nav"}},[n("router-link",{attrs:{to:"/"}},[e._v("Home")]),e._v(" | "),n("router-link",{attrs:{to:"/about"}},[e._v("About")])],1),n("router-view")],1)},s=[],i=(n("5c0b"),n("2877")),l={},c=Object(i["a"])(l,o,s,!1,null,null,null),m=c.exports,p=n("9483");Object(p["a"])("".concat("/","service-worker.js"),{ready:function(){console.log("App is being served from cache by a service worker.\nFor more details, visit https://goo.gl/AFskqB")},registered:function(){console.log("Service worker has been registered.")},cached:function(){console.log("Content has been cached for offline use.")},updatefound:function(){console.log("New content is downloading.")},updated:function(){console.log("New content is available; please refresh.")},offline:function(){console.log("No internet connection found. App is running in offline mode.")},error:function(e){console.error("Error during service worker registration:",e)}});n("d3b7"),n("3ca3"),n("ddb0");var u=n("8c4f"),d=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"home"},[n("XmlForm",{attrs:{xsdFile:e.xmlData}})],1)},f=[],h='<schema attributeFormDefault="unqualified" elementFormDefault="qualified"\n  xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://GroupName-017/temporary"\n  xmlns:sample="http://GroupName-017/temporary">\n  <element name="ETL" type="sample:ETLType" />\n  <complexType name="sourceinfoType">\n    <sequence>\n      <choice>\n        <element name="SQL" type="sample:sqlProtocolType"/>\n\n        <element name="FTP" type="sample:ftpProtocolType"/>\n      </choice>\n    </sequence>\n  </complexType>\n\n  <complexType name="sqlProtocolType">\n    <sequence>\n      <element type="string" name="name" />\n      <element type="string" name="driver" />\n      <element type="string" name="username" />\n      <element type="string" name="password" />\n    </sequence>\n  </complexType>\n\n  <complexType name="ftpProtocolType">\n    <sequence>\n      <element type="string" name="username" />\n      <element type="string" name="password" />\n      <element type="string" name="ip-address"/>\n    </sequence>\n  </complexType>\n\n\n\n  <complexType name="sourceDetailsType">\n    <sequence>\n      <element type="sample:sourceinfoType" name="sourceinfo" />\n    </sequence>\n  </complexType>\n\n\n  <complexType name="Extract">\n    <sequence >\n      <element type="string" name="Query"/>\n      <element type="string" name="DstTable"/>\n\n    </sequence>\n  </complexType>\n\n\n  <complexType name="TextTransformationType">\n    <sequence >\n      <element type="string" name="sourceAttribute" />\n      <element type="string" name="destinationAttribute"/>\n\n      <element type="string" name="sourcePattern" />\n      <element type="string" name="destinationPattern" />\n    </sequence>\n  </complexType>\n\n\n  <complexType name="ArthimeticTransformationType">\n    <sequence>\n      <element type="string" name="sourceAttribute" />\n      <element type="string" name="destinationAttribute"/>\n\n      <element type="string" name="arthimeticFormulae" />\n    </sequence>\n  </complexType>\n\n  <complexType name="NullTransformationType">\n    <sequence>\n      <element type="string" name="sourceAttribute" />\n      <element type="string" name="destinationAttribute" />\n    </sequence>\n  </complexType>\n\n\n  <complexType name="TransformationDetailsType">\n<choice minOccurs="0" maxOccurs="unbounded">\n      <element type="sample:TextTransformationType" name="TextTransformation" />\n      <element type="sample:ArthimeticTransformationType" name="ArthimeticTransformation" />\n      <element type="sample:NullTransformationType" name="NullTransformation" />\n\n\n    </choice>\n  </complexType>\n\n\n  <complexType name="DestinationInfoType">\n    <sequence>\n      <element type="string" name="name" />\n      <element type="string" name="driver" />\n      <element type="string" name="protocol" />\n      <element type="string" name="username" />\n      <element type="string" name="password" />\n    </sequence>\n  </complexType>\n\n  <complexType name="DestinationDetailsType">\n    <sequence>\n      <element type="sample:DestinationInfoType" name="DestinationInfo" />\n\n    </sequence>\n  </complexType>\n  <complexType name="EtType">\n    <sequence>\n      <element type="sample:sourceDetailsType" name="sourceDetails"/>\n      <element type="sample:Extract" name="ExtractSequence" />\n<element type="sample:TransformationDetailsType" name="TransformationDetails"/>\n\n\n\n    </sequence>\n  </complexType>\n\n  <complexType name="ETLType">\n    <sequence>\n      <element type="sample:EtType" name="ET" minOccurs="1" maxOccurs="unbounded"/>\n      <element type="sample:DestinationDetailsType" name="DestinationDetails"/>\n\n\n\n    </sequence>\n  </complexType>\n</schema>',y=function(){var e=this,t=e.$createElement,n=e._self._c||t;return e.show?n("b-container",{staticClass:"main-form",staticStyle:{padding:"0px"},attrs:{fluid:""}},[n("b-form",{on:{submit:e.getXML}},[n("b-row",{staticClass:"my-4"},[n("b-col",[n("b-button",[e._v("Back")])],1),n("b-col",[n("b-button",{attrs:{type:"submit"}},[e._v("Run")])],1)],1),n("XmlElementForm",{key:e.getJson.schema.element.name,ref:"xmlForm",staticClass:"shadow",attrs:{name:e.getJson.schema.element.name,type:e.getJson.schema.element.type,parentType:"",idx:"0"}})],1)],1):e._e()},b=[],g=n("5530"),x=(n("b0c0"),n("159b"),n("fb6a"),n("a15b"),n("7a51")),v=n.n(x),T=n("2f62"),w=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",["string"===e.type?n("div",{staticClass:"d-flex"},[n("div",{staticClass:"w-25"}),n("b-form-group",{staticClass:"mb-0 form",attrs:{label:e.name,"label-cols-sm":"3","content-cols-sm":"","label-class":"font-weight-bold pt-3","label-for":e.name+e.type+e.parentType+e.idx}},[n("b-form-input",{ref:"formInput",staticStyle:{"margin-left":"10px","margin-right":"10px","margin-top":"10px","margin-bottom":"10px"},attrs:{id:e.name+e.parentType+e.idx,required:0!==e.min},model:{value:e.formValue,callback:function(t){e.formValue=t},expression:"formValue"}})],1)],1):n("b-card",{staticClass:"mb-2 form",style:""==e.parentType?"border:none;":""},[n("b-card-title",{staticStyle:{"text-align":"start","margin-left":"10px"}},[e._v(e._s(e.name))]),e.elementPresent?n("div",[e.isElementObject()?n("div",[e.checkMinMax(e.childEleProto)?n("b-row",{attrs:{"align-h":"end"}},[n("b-button",{on:{click:e.duplicatedElem}},[e._v("plus")])],1):e._e(),e._l(e.childEle,(function(t,r){return n("b-row",{key:r},[n("b-col",[n("XmlElementForm",{key:e.checkMinMax(t)?t.name+r:t.name,ref:"elems",refInFor:!0,attrs:{name:t.name,type:t.type,parentType:e.getType.name,idx:r+e.idx,min:t.minOccurs,max:t.maxOccurs}})],1),0!=r?n("b-col",{attrs:{lg:"2"}},[n("b-button",{on:{click:function(t){return e.deleteElem(r)}}},[e._v("delete")])],1):e.checkMinMax(e.childEleProto)&&0==r?n("b-col",{attrs:{lg:"2"}}):e._e()],1)}))],2):n("div",e._l(e.childEle,(function(t,r){return n("b-row",{key:t.id},[n("b-col",[n("XmlElementForm",{key:t.name+t.id,ref:"elems",refInFor:!0,attrs:{name:t.name,type:t.type,parentType:e.getType.name,min:t.minOccurs,max:t.maxOccurs,idx:t.id+e.idx}})],1),e.checkMinMax(t)?n("b-col",{attrs:{md:"auto"}},[n("b-button",{attrs:{variant:"link"},on:{click:function(n){return e.addElem(t,r)}}},[n("svg",{staticClass:"bi bi-plus",attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",fill:"currentColor",viewBox:"0 0 16 16"}},[n("path",{attrs:{d:"M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"}})])])],1):e._e(),e.checkMinMax(t)&&1!==e.checkItemIndex(t)?n("b-col",{attrs:{md:"auto"}},[n("b-button",{attrs:{variant:"link"},on:{click:function(t){return e.deleteElem(r)}}},[n("svg",{staticClass:"bi bi-trash-fill",staticStyle:{"margin-top":"2px"},attrs:{xmlns:"http://www.w3.org/2000/svg",width:"16",height:"16",fill:"currentColor",viewBox:"0 0 16 16"}},[n("path",{attrs:{d:"M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"}})])])],1):e._e()],1)})),1)]):e.choiceSeqPresent?n("div",{staticClass:"form"},[e.checkMinMax(e.childEleProto)?n("b-row",{attrs:{"align-h":"end"}},[n("b-button",{on:{click:e.duplicatedElem}},[e._v("plus")])],1):e._e(),n("b-form-radio-group",{attrs:{required:0!==e.min},model:{value:e.selectedArray[0],callback:function(t){e.$set(e.selectedArray,0,t)},expression:"selectedArray[0]"}},e._l(e.getType.sequence.choice.element,(function(t){return n("b-form-radio",{key:t.name,attrs:{value:t}},[e._v(e._s(t.name)+" ")])})),1),Object.keys(e.selectedArray[0]).length>0?n("div",e._l(e.selectedArray,(function(t){return n("div",{key:t.name},[n("XmlElementForm",{key:t.name,ref:"elems",refInFor:!0,attrs:{name:t.name,type:t.type,parentType:e.getType.name,min:t.minOccurs,max:t.maxOccurs,idx:e.idx}})],1)})),0):e._e()],1):e.choicePresent?n("div",{staticClass:"form"},[e.checkMinMax(e.getType.choice)?n("b-row",{attrs:{"align-h":"end"}},[n("b-button",{attrs:{variant:"link"},on:{click:e.selfDuplicate}},[n("svg",{staticClass:"bi bi-plus",attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",fill:"currentColor",viewBox:"0 0 16 16"}},[n("path",{attrs:{d:"M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"}})])])],1):e._e(),e._l(e.selfEle,(function(t,r){return n("div",{key:r},[n("b-row",{attrs:{"align-h":"center"}},[n("b-form-radio-group",{attrs:{required:0!==e.min},model:{value:e.selectedArray[r],callback:function(t){e.$set(e.selectedArray,r,t)},expression:"selectedArray[index]"}},e._l(e.getType.choice.element,(function(t){return n("b-form-radio",{key:t.name+e.idx,attrs:{value:t}},[e._v(e._s(t.name))])})),1),0!=r?n("b-col",{attrs:{md:"auto"}},[n("b-button",{attrs:{variant:"link"},on:{click:function(t){return e.selfDelete(r)}}},[n("svg",{staticClass:"bi bi-trash-fill",staticStyle:{"margin-top":"2px"},attrs:{xmlns:"http://www.w3.org/2000/svg",width:"16",height:"16",fill:"currentColor",viewBox:"0 0 16 16"}},[n("path",{attrs:{d:"M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"}})])])],1):n("b-col",{staticStyle:{width:"72px",height:"38px","padding-left":"15px","padding-right":"15px"},attrs:{md:"auto"}})],1),Object.keys(e.selectedArray[r]).length>0?n("div",{staticClass:"form"},[n("XmlElementForm",{key:e.selectedArray[r].name+e.idx,ref:"elems",refInFor:!0,attrs:{name:e.selectedArray[r].name,type:e.selectedArray[r].type,parentType:e.getType.name,min:e.selectedArray[r].minOccurs,max:e.selectedArray[r].maxOccurs,idx:r}})],1):e._e()],1)}))],2):e._e()],1)],1)},E=[],O=(n("a434"),n("4de4"),n("7db0"),n("5319"),n("ac1f"),{name:"XmlElementForm",props:["name","type","parentType","idx","min","max"],data:function(){return{selected:{},selectedArray:[],childEle:[],childEleProto:{},selfEle:[],formValue:"",id:0}},beforeMount:function(){this.selfEle.push(0),this.selectedArray.push(this.selected)},mounted:function(){},methods:{duplicatedElem:function(){this.childEle.push(this.childEleProto)},selfDuplicate:function(){this.selfEle.push(0),this.selectedArray.push(this.selected)},deleteElem:function(e){this.$delete(this.childEle,e)},addElem:function(e,t){var n=JSON.parse(JSON.stringify(e));n.id=this.id++,this.childEle.splice(t+1,0,n)},selfDelete:function(e){this.selfEle.splice(e,1),this.selectedArray.splice(e,1)},checkItemIndex:function(e){return this.childEle.filter((function(t){return t.name===e.name})).length},checkMinMax:function(e){return!(!Object.prototype.hasOwnProperty.call(e,"minOccurs")&&!Object.prototype.hasOwnProperty.call(e,"maxOccurs"))&&(0===this.childEle.length&&(this.childEle.push(e),this.childEleProto=e),!0)},isElementObject:function(){var e=this;return!!this.elementPresent&&(this.getType.sequence.element&&this.getType.sequence.element.constructor===Object?(0===this.childEle.length&&(this.childEle.push(this.getType.sequence.element),this.childEleProto=this.getType.sequence.element),!0):(0===this.childEle.length&&this.getType.sequence.element.forEach((function(t){t.id=e.id++,e.childEle.push(t)})),!1))}},computed:Object(g["a"])({getComplexTypeData:function(){return this.complexTypeData},getType:function(){var e=this;return"string"==this.type?this.type:this.complexTypeData.find((function(t){return t.name===e.type.replace(/^sample:/,"")}))},sequencePresent:function(){return Object.prototype.hasOwnProperty.call(this.getType,"sequence")},elementPresent:function(){return!!this.sequencePresent&&Object.prototype.hasOwnProperty.call(this.getType.sequence,"element")},choiceSeqPresent:function(){return!!this.sequencePresent&&Object.prototype.hasOwnProperty.call(this.getType.sequence,"choice")},choicePresent:function(){return Object.prototype.hasOwnProperty.call(this.getType,"choice")}},Object(T["b"])(["complexTypeData"]))}),k=O,q=(n("300d"),Object(i["a"])(k,w,E,!1,null,"e5e8b556",null)),_=q.exports,A=r["default"].extend({name:"XsdForm",props:{xsdFile:String},data:function(){return{show:!0}},components:{XmlElementForm:_},methods:{generateXml:function(e,t){var n=this;"elems"in e.$refs?(t.push("<"+e.$props.name+">"),e.$refs.elems.forEach((function(e){n.generateXml(e,t)})),t.push("</"+e.$props.name+">")):"formInput"in e.$refs&&(t.push("<"+e.$props.name+">"),t.push(e.formValue),t.push("</"+e.$props.name+">"))},getXML:function(e){e.preventDefault();var t=['<?xml version="1.0" encoding="utf-8" ?>'];this.generateXml(this.$refs.xmlForm,t),t[1]=t[1].slice(0,-1)+' xmlns ="'+this.getJson.schema.targetNamespace+'" >';var n=t.join("\n");this.$store.dispatch("addXmlFile",n)},onReset:function(e){var t=this;e.preventDefault(),this.show=!1,this.$nextTick((function(){t.show=!0}))}},computed:Object(g["a"])({options:function(){return{attributeNamePrefix:"",ignoreAttributes:!1,ignoreNameSpace:!1,allowBooleanAttributes:!0,parseNodeValue:!0,parseAttributeValue:!0,trimValues:!0,parseTrueNumberOnly:!0,arrayMode:!1}},getJson:function(){var e=v.a.validate(this.xsdFile);!0!==e&&console.log(e.err);var t=v.a.parse(this.xsdFile,this.options);return t}},Object(T["b"])(["complexTypeData"])),mounted:function(){}}),P=A,D=(n("2748"),Object(i["a"])(P,y,b,!1,null,"65836da5",null)),j=D.exports,F=r["default"].extend({components:{XmlForm:j},data:function(){return{xmlData:h}}}),M=F,C=Object(i["a"])(M,d,f,!1,null,null,null),S=C.exports;r["default"].use(u["a"]);var N=[{path:"/",name:"Home",component:S},{path:"/about",name:"About",component:function(){return n.e("about").then(n.bind(null,"f820"))}}],X=new u["a"]({mode:"history",base:"/",routes:N}),$=X,V=n("bc3a"),I=n.n(V);r["default"].use(T["a"]);var z={attributeNamePrefix:"",ignoreAttributes:!1,ignoreNameSpace:!1,allowBooleanAttributes:!0,parseNodeValue:!0,parseAttributeValue:!0,trimValues:!0,parseTrueNumberOnly:!0,arrayMode:!1},H=v.a.parse(h,z),J=new T["a"].Store({state:{complexTypeData:H.schema.complexType,xmlFile:""},mutations:{addComplexTypeData:function(e,t){e.complexTypeData.push(t)},addXmlFile:function(e,t){e.xmlFile=t}},actions:{addXmlFile:function(e,t){var n=e.commit;e.state;n("addXmlFile",t),I()({method:"post",url:"http://localhost:5000/api/xmlFile",data:t})}},modules:{},getters:{type:function(e){return function(t){return e.complexTypeData.find((function(e){return e.name===t.replace(/^sample:/,"")}))}}}});r["default"].config.productionTip=!1,new r["default"]({router:$,store:J,render:function(e){return e(m)}}).$mount("#app")},e386:function(e,t,n){}});
//# sourceMappingURL=app.4c01384b.js.map