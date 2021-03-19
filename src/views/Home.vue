<template>
  <div class="home">
    <!-- <img
      alt="Vue logo"
      src="../assets/logo.png"
    /> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App" /> -->
    <XmlForm :xsdFile="xmlData" />
  </div>
</template>

<script lang="ts">
// import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src
import xmlData from "!!raw-loader!@/assets/template.xsd";
import XmlForm from "@/components/XsdForm.vue";
import Vue from "vue";

export default Vue.extend({
  components: {
    // HelloWorld,
    XmlForm
  },
  data() {
    return { xmlData: xmlData };
  }
});
</script>
