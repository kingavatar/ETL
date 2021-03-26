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
    <div
      v-if="type === 'string'"
      class="d-flex"
    >
      <div class="w-25" />
      <b-form-group
        :label="name"
        label-cols-sm="3"
        content-cols-sm
        label-class="font-weight-bold pt-3"
        :label-for="name+type+parentType+idx"
        class="mb-0 form"
      >
        <b-form-input
          style="margin-left:10px;margin-right:10px;margin-top:10px;margin-bottom:10px;"
          :id="name+type+parentType+idx"
        ></b-form-input>
      </b-form-group>
    </div>
    <b-card
      v-else
      class="mb-2 form"
      style=""
    >
      <b-card-title style="text-align:start; margin-left:10px;">{{
        name
      }}</b-card-title>
      <b-row class="form">
        <!-- label-cols-lg="2" -->
        <div class="form">
          <div v-if="elementPresent">
            <div v-if="isElementObject && !checkMinMax(getType.sequence.element)">
              <XmlElementForm
                :name="getType.sequence.element.name"
                :type="getType.sequence.element.type"
                :parentType="getType.name"
                idx=""
              />
            </div>
            <div v-else-if="isElementObject && checkMinMax(getType.sequence.element)">
              <b-row>
                <b-col>
                  <XmlElementForm
                    v-for="(item,index) in childEle"
                    v-bind:key="index"
                    :name="item.name"
                    :type="item.type"
                    :parentType="getType.name"
                    :idx="index"
                    :min="item.minOccurs"
                    :max="item.maxOccurs"
                  />
                </b-col>
                <b-col lg="2">
                  <b-button @click="duplicatedElem">plus</b-button>
                </b-col>
              </b-row>
            </div>
            <div
              v-else
              class="form"
            >
              <XmlElementForm
                v-for="item in getType.sequence.element"
                v-bind:key="item.name"
                :name="item.name"
                :type="item.type"
                :parentType="getType.name"
                idx=""
              />
            </div>
          </div>
          <div
            v-else-if="choiceSeqPresent"
            class="form"
          >
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
                :name="selected.name"
                :type="selected.type"
                :parentType="getType.name"
                idx=""
              />
            </div>
            <!-- :complexTypeData="getComplexTypeData" -->
          </div>
          <div
            v-else-if="choicePresent"
            class="form"
          >
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
              >{{ choiceItem.name }}</b-form-radio>
            </b-form-radio-group>
            <div
              v-if="Object.keys(selected).length > 0"
              class="form"
            >
              <XmlElementForm
                :name="selected.name"
                :type="selected.type"
                :parentType="getType.name"
                idx=""
              />
            </div>
            <!-- :complexTypeData="getComplexTypeData" -->
          </div>
        </div>
      </b-row>
    </b-card>
    <!-- </b-form-group> -->
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "XmlElementForm",
  props: ["name", "type", "parentType", "idx", "min", "max"],
  data () {
    return {
      selected: {},
      childEle: [],
      childEleProto: {}
    };
  },
  mounted () {
    console.log(this.name, this.type, this.parentType, this.idx, this.childEle);
  },
  methods: {
    duplicatedElem() {
      console.log(this.childEleProto);
      this.childEle.push(this.childEleProto);
    },
    checkMinMax (obj) {
      if (Object.prototype.hasOwnProperty.call(obj, "minOccurs") || Object.prototype.hasOwnProperty.call(obj, "maxOccurs")) {
        if (this.childEle.length === 0) {
          this.childEle.push(obj);
          this.childEleProto = obj;
        }
        return true;
      }
      return false;
    }
  },
  computed: {
    getComplexTypeData () {
      return this.complexTypeData;
    },
    getType () {
      return this.complexTypeData.find(
        x => x.name === this.type.replace(/^sample:/, "")
      );
    },
    isElementObject () {
      if (this.elementPresent) {
        return (
          !!this.getType.sequence.element &&
          this.getType.sequence.element.constructor === Object
        );
      } else {
        return false;
      }
    },
    sequencePresent () {
      return Object.prototype.hasOwnProperty.call(this.getType, "sequence");
    },
    elementPresent () {
      if (this.sequencePresent) {
        return Object.prototype.hasOwnProperty.call(
          this.getType.sequence,
          "element"
        );
      }
      return false;
    },
    choiceSeqPresent () {
      if (this.sequencePresent) {
        return Object.prototype.hasOwnProperty.call(
          this.getType.sequence,
          "choice"
        );
      }
      return false;
    },
    choicePresent () {
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
