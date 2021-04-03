<template>
  <div class="form">
    <!-- <b-form-group
      label-cols-lg="2"
      :label="name"
      label-class="font-weight-bold pt-0"
      class="mb-0"
    > -->
    <!-- label-cols-lg="3" -->
    <!-- content-cols-lg="7" -->
    <div v-if="type === 'string'" class="d-flex">
      <div class="w-25" />
      <b-form-group
        :label="name"
        label-cols-sm="3"
        content-cols-sm
        label-class="font-weight-bold pt-3"
        :label-for="name + type + parentType + idx"
        class="mb-0 form"
      >
        <b-form-input
          ref="formInput"
          v-model="formValue"
          style="margin-left:10px;margin-right:10px;margin-top:10px;margin-bottom:10px;"
          :id="name + parentType + idx"
        ></b-form-input>
      </b-form-group>
    </div>
    <b-card
      v-else
      class="mb-2 form"
      :style="parentType == '' ? 'border:none;' : ''"
    >
      <b-card-title style="text-align:start; margin-left:10px;">{{
        name
      }}</b-card-title>
      <!-- <b-row class="form"> -->
      <!-- <div class="form"> -->
      <div v-if="elementPresent">
        <!-- <div v-if="isElementObject() && !checkMinMax(getType.sequence.element)">
              <XmlElementForm
                :name="getType.sequence.element.name"
                :type="getType.sequence.element.type"
                :parentType="getType.name"
                idx=""
              />
            </div> -->
        <div v-if="isElementObject()">
          <b-row v-if="checkMinMax(childEleProto)" align-h="end">
            <b-button @click="duplicatedElem">plus</b-button>
          </b-row>
          <b-row v-for="(item, index) in childEle" v-bind:key="index">
            <b-col>
              <XmlElementForm
                v-bind:key="checkMinMax(item) ? item.name + index : item.name"
                :name="item.name"
                :type="item.type"
                :parentType="getType.name"
                :idx="index"
                :min="item.minOccurs"
                :max="item.maxOccurs"
                ref="elems"
              />
            </b-col>
            <b-col v-if="index != 0" lg="2">
              <b-button @click="deleteElem(index)">delete</b-button>
            </b-col>
            <b-col
              v-else-if="checkMinMax(childEleProto) && index == 0"
              lg="2"
            ></b-col>
          </b-row>
        </div>
        <div v-else class="form">
          <XmlElementForm
            v-for="item in getType.sequence.element"
            v-bind:key="item.name"
            :name="item.name"
            :type="item.type"
            :parentType="getType.name"
            :min="item.minOccurs"
            :max="item.maxOccurs"
            ref="elems"
            idx=""
          />
        </div>
      </div>
      <div v-else-if="choiceSeqPresent" class="form">
        <b-row v-if="checkMinMax(childEleProto)" align-h="end">
          <b-button @click="duplicatedElem">plus</b-button>
        </b-row>
        <b-form-radio-group
          :id="type"
          v-model="selected"
          name="radio-choiceSeq"
        >
          <b-form-radio
            v-for="choiceItem in getType.sequence.choice.element"
            v-bind:key="choiceItem.name"
            :value="choiceItem"
            >{{ choiceItem.name }}
          </b-form-radio>
        </b-form-radio-group>
        <div v-if="Object.keys(selected).length > 0">
          <XmlElementForm
            v-bind:key="selected.name"
            :name="selected.name"
            :type="selected.type"
            :parentType="getType.name"
            :min="selected.minOccurs"
            :max="selected.maxOccurs"
            ref="elems"
            idx=""
          />
        </div>
        <!-- :complexTypeData="getComplexTypeData" -->
      </div>
      <div v-else-if="choicePresent" class="form">
        <!-- <h3>choice check</h3> -->
        <!-- <h3 v-if="checkSelfMinMax">min max check</h3> -->
        <b-row v-if="checkSelfMinMax" align-h="end">
          <b-button @click="selfDuplicate">plus</b-button>
        </b-row>
        <div v-for="(_, index) in selfEle" v-bind:key="index">
          <b-row align-h="center">
            <b-form-radio-group
              :id="type + index"
              v-model="selectedArray[index]"
              :name="'radio-choice' + index"
            >
              <b-form-radio
                v-for="choiceItem in getType.choice.element"
                v-bind:key="choiceItem.name + index"
                :value="choiceItem"
                >{{ choiceItem.name }}</b-form-radio
              >
            </b-form-radio-group>
            <b-col v-if="index != 0" lg="2">
              <b-button @click="selfDelete(index)">delete</b-button>
            </b-col>
          </b-row>
          <div v-if="Object.keys(selectedArray[index]).length > 0" class="form">
            <XmlElementForm
              v-bind:key="selectedArray[index].name + index"
              :name="selectedArray[index].name"
              :type="selectedArray[index].type"
              :parentType="getType.name"
              :min="selectedArray[index].minOccurs"
              :max="selectedArray[index].maxOccurs"
              ref="elems"
              :idx="index"
            />
          </div>
        </div>
        <!-- :complexTypeData="getComplexTypeData" -->
      </div>
      <!-- </div> -->
      <!-- </b-row> -->
    </b-card>
    <!-- </b-form-group> -->
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "XmlElementForm",
  props: ["name", "type", "parentType", "idx", "min", "max"],
  data() {
    return {
      selected: {},
      selectedArray: [],
      childEle: [],
      childEleProto: {},
      selfEle: [],
      formValue: ""
    };
  },
  beforeMount() {
    this.selfEle.push(0);
    this.selectedArray.push(this.selected);
  },
  mounted() {
    console.log(this.name, this.type, this.childEle);
  },
  methods: {
    duplicatedElem() {
      this.childEle.push(this.childEleProto);
    },
    selfDuplicate() {
      if (this.checkSelfMinMax) {
        this.selfEle.push(0);
        this.selectedArray.push(this.selected);
      }
    },
    deleteElem(index) {
      this.childEle.splice(index, 1);
    },
    selfDelete(index) {
      this.selfEle.splice(index, 1);
      this.selectedArray.splice(index, 1);
    },
    checkMinMax(obj) {
      if (
        Object.prototype.hasOwnProperty.call(obj, "minOccurs") ||
        Object.prototype.hasOwnProperty.call(obj, "maxOccurs")
      ) {
        if (this.childEle.length === 0) {
          this.childEle.push(obj);
          this.childEleProto = obj;
        }
        return true;
      }
      return false;
    },
    isElementObject() {
      if (this.elementPresent) {
        if (
          !!this.getType.sequence.element &&
          this.getType.sequence.element.constructor === Object
        ) {
          if (this.childEle.length === 0) {
            this.childEle.push(this.getType.sequence.element);
            this.childEleProto = this.getType.sequence.element;
          }
          return true;
        }
        return false;
      } else {
        return false;
      }
    }
  },
  computed: {
    getComplexTypeData() {
      return this.complexTypeData;
    },
    getType() {
      if (this.type == "string") {
        return this.type;
      }
      return this.complexTypeData.find(
        x => x.name === this.type.replace(/^sample:/, "")
      );
    },
    checkSelfMinMax() {
      if (this.min != undefined || this.max != undefined) {
        return true;
      }
      return false;
    },
    sequencePresent() {
      return Object.prototype.hasOwnProperty.call(this.getType, "sequence");
    },
    elementPresent() {
      if (this.sequencePresent) {
        return Object.prototype.hasOwnProperty.call(
          this.getType.sequence,
          "element"
        );
      }
      return false;
    },
    choiceSeqPresent() {
      if (this.sequencePresent) {
        return Object.prototype.hasOwnProperty.call(
          this.getType.sequence,
          "choice"
        );
      }
      return false;
    },
    choicePresent() {
      return Object.prototype.hasOwnProperty.call(this.getType, "choice");
    },
    ...mapState(["complexTypeData"])
  }
};
</script>

<style lang="scss" scoped>
.form {
  width: 100%;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
</style>
