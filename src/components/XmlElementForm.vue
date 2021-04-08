<template>
  <div>
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
          :required="min !== 0"
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
                :idx="index + idx"
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
        <div v-else>
          <b-row v-for="(item, index) in childEle" v-bind:key="item.id">
            <!-- v-for="item in getType.sequence.element"
            v-bind:key="item.name" -->
            <b-col>
              <XmlElementForm
                v-bind:key="item.name + item.id"
                :name="item.name"
                :type="item.type"
                :parentType="getType.name"
                :min="item.minOccurs"
                :max="item.maxOccurs"
                :idx="item.id + idx"
                ref="elems"
              />
            </b-col>
            <b-col v-if="checkMinMax(item)" md="auto">
              <!-- <p>{{item.name}}</p> -->
              <b-button variant="link" @click="addElem(item, index)">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="bi bi-plus"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
                  />
                </svg>
              </b-button>
            </b-col>
            <b-col
              v-if="checkMinMax(item) && checkItemIndex(item) !== 1"
              md="auto"
            >
              <!-- <p>{{item.name}}</p> -->
              <b-button variant="link" @click="deleteElem(index)">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-trash-fill"
                  style="margin-top:2px;"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"
                  />
                </svg>
              </b-button>
            </b-col>
            <!-- <div v-if="checkMinMax(item)"/> -->
          </b-row>
        </div>
      </div>
      <div v-else-if="choiceSeqPresent" class="form">
        <b-row v-if="checkMinMax(childEleProto)" align-h="end">
          <b-button @click="duplicatedElem">plus</b-button>
        </b-row>
        <!-- :id="type" -->
        <!-- name="radio-choiceSeq" -->
        <b-form-radio-group v-model="selectedArray[0]" :required="min !== 0">
          <b-form-radio
            v-for="choiceItem in getType.sequence.choice.element"
            v-bind:key="choiceItem.name"
            :value="choiceItem"
            >{{ choiceItem.name }}
          </b-form-radio>
        </b-form-radio-group>
        <div v-if="Object.keys(selectedArray[0]).length > 0">
          <div v-for="item in selectedArray" v-bind:key="item.name">
            <XmlElementForm
              v-bind:key="item.name"
              :name="item.name"
              :type="item.type"
              :parentType="getType.name"
              :min="item.minOccurs"
              :max="item.maxOccurs"
              ref="elems"
              :idx="idx"
            />
          </div>
        </div>
        <!-- :complexTypeData="getComplexTypeData" -->
      </div>
      <div v-else-if="choicePresent" class="form">
        <!-- <h3>choice check</h3> -->
        <!-- <h3 v-if="checkSelfMinMax">min max check</h3> -->
        <!-- <b-row v-if="checkSelfMinMax" align-h="end">
          <b-button @click="selfDuplicate">plus</b-button>
        </b-row> -->
        <!-- <div v-for="(_, index) in selfEle" v-bind:key="index"> -->
        <b-row align-h="center">
          <!-- :id="type + idx" -->
          <!-- :name="'radio-choice' + idx" -->
          <b-form-radio-group v-model="selectedArray[0]" :required="min !== 0">
            <b-form-radio
              v-for="choiceItem in getType.choice.element"
              v-bind:key="choiceItem.name + idx"
              :value="choiceItem"
              >{{ choiceItem.name }}</b-form-radio
            >
          </b-form-radio-group>
          <!-- <b-col v-if="index != 0" lg="2">
              <b-button @click="selfDelete(index)">delete</b-button>
            </b-col> -->
        </b-row>
        <div v-if="Object.keys(selectedArray[0]).length > 0" class="form">
          <div v-for="item in selectedArray" v-bind:key="item.name">
            <XmlElementForm
              v-bind:key="item.name + idx"
              :name="item.name"
              :type="item.type"
              :parentType="getType.name"
              :min="item.minOccurs"
              :max="item.maxOccurs"
              ref="elems"
              :idx="idx"
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
      formValue: "",
      id: 0
    };
  },
  beforeMount() {
    this.selfEle.push(0);
    this.selectedArray.push(this.selected);
  },
  mounted() {
    // console.log(this.name, this.type, this.childEle);
  },
  methods: {
    duplicatedElem() {
      this.childEle.push(this.childEleProto);
    },
    // selfDuplicate() {
    //   if (this.checkSelfMinMax) {
    //     this.selfEle.push(0);
    //     this.selectedArray.push(this.selected);
    //   }
    // },
    deleteElem(index) {
      // this.childEle.splice(index, 1);
      this.$delete(this.childEle, index);
    },
    addElem(item, index) {
      const temp = JSON.parse(JSON.stringify(item));
      temp.id = this.id++;
      this.childEle.splice(index + 1, 0, temp);
    },
    // selfDelete(index) {
    //   this.selfEle.splice(index, 1);
    //   this.selectedArray.splice(index, 1);
    // },
    checkItemIndex(item) {
      return this.childEle.filter(x => x.name === item.name).length;
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
        if (this.childEle.length === 0)
          this.getType.sequence.element.forEach(item => {
            item.id = this.id++;
            this.childEle.push(item);
          });
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
.btn-link {
  // color: initial;
  box-shadow: none;
}
</style>
