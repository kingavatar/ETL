<template>
  <div>
    <b-form-group
      label-cols-lg="2"
      :label="name"
      label-class="font-weight-bold pt-0"
      class="mb-0"
    >
    <b-form-input
        v-if="type=='string'"
        style="margin-left:10px;margin-right:10px;margin-top:10px;margin-bottom:10px;"
        :id="type+name"
      ></b-form-input>
      <div v-else>
      <div v-if="elementPresent">
        <!-- <h3>element check</h3> -->
        <div 
          v-if="isElementObject">
         <XmlElementForm
          :name="getType.sequence.element.name"
          :type="getType.sequence.element.type"
        />
        </div>
        <div v-else>
          <XmlElementForm
          v-for="item in getType.sequence.element"
          v-bind:key="item.name"
          :name="item.name"
          :type="item.type"
        />
        </div>
      </div>
      <div v-else-if="choiceSeqPresent">
        <!-- <h3>choice Sequnce check</h3> -->
        <b-form-radio-group
          :id="type"
          v-model="selected"
          name="radio-choiceSeq"
        >
          <b-form-radio
            v-for="choiceItem in getType.sequence.choice.element"
            v-bind:key="choiceItem.name"
            :value="choiceItem"
          >{{choiceItem.name}}</b-form-radio>
        </b-form-radio-group>
        <div
          v-if="Object.keys(selected).length>0"
        >
        <!-- <p>selected {{selected}} </p> -->
        <XmlElementForm
          :name="selected.name"
          :type="selected.type"
        />
        </div>
          <!-- :complexTypeData="getComplexTypeData" -->
      </div>
      <div v-else-if="choicePresent">
        <!-- <h3>choice check</h3> -->
        <b-form-radio-group
          :id="type"
          v-model="selected"
          name="radio-choice"
        >
          <b-form-radio
            v-for="choiceItem in getType.choice.element"
            v-bind:key="choiceItem.name"
            :value="choiceItem"
          >{{choiceItem.name}}</b-form-radio>
        </b-form-radio-group>
        <div 
          v-if="Object.keys(selected).length>0"
        >
        <!-- <p>selected {{selected}} </p> -->

        <XmlElementForm
          :name="selected.name"
          :type="selected.type"
        />
        </div>
          <!-- :complexTypeData="getComplexTypeData" -->
      </div>
      </div>
    </b-form-group>

  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: "XmlElementForm",
  props: [
    'name',
    'type']
  ,
  data () {
    return {
      selected: {}
    }
  },
  mounted(){
    console.log(this.name,this.type);
  },
  computed: {
    getComplexTypeData(){
      return this.complexTypeData;
    },
    getType () {
      return this.complexTypeData.find(x => x.name === this.type.replace(/^sample:/, ''));
    },
    isElementObject(){
      if(this.elementPresent){
      return (!!this.getType.sequence.element) && (this.getType.sequence.element.constructor === Object);}
      else {return false;}
    },
    sequencePresent () {
      return Object.prototype.hasOwnProperty.call(this.getType, 'sequence')
    },
    elementPresent () {
      if (this.sequencePresent) {
        return Object.prototype.hasOwnProperty.call(this.getType.sequence, 'element');
      }
      return false;
    },
    choiceSeqPresent () {
      if (this.sequencePresent) {
        return Object.prototype.hasOwnProperty.call(this.getType.sequence, 'choice');
      }
      return false;
    },
    choicePresent () {
        return Object.prototype.hasOwnProperty.call(this.getType, 'choice');
    },
    ...mapState([
      'complexTypeData'
    ])
  }
};


</script>

<style lang="scss" scoped>
</style>