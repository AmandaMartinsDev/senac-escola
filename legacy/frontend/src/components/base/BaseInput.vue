<template>
  <div
    :style="{ width: width }"
    @mouseenter="mouseOver = true"
    @mouseleave="mouseOver = false"
  >
    <input
      :type="type"
      :placeholder="placeholder"
      :value="inputValue"
      @keyup="($event) => onKeyUp($event)"
    />
    <img
      :class="{ active: inputValue.trim() && mouseOver, iconClear: true }"
      src="../../assets/cross.svg"
      @click="clear()"
    />
  </div>
</template>

<script lang="ts">
export default {
  props: {
    type: {
      type: String,
      default: "text",
    },
    placeholder: {
      type: String,
      default: "",
    },
    value: {
      type: String,
      default: "",
    },
    width: {
      type: String,
      default: "100%",
    },
  },
  data() {
    return {
      inputValue: this.value,
      mouseOver: false,
    };
  },
  methods: {
    onKeyUp(event: any) {
      this.inputValue = event.target.value;
      this.$emit("onKeyUp", event.target.value);
    },
    clear() {
      this.inputValue = "";
      this.$emit("onKeyUp", "");
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../styles/scss/variables.scss";

div {
  position: relative;
  height: $base-height;

  input {
    background: $branco;
    border: 1px solid $cinza-claro;
    color: $cinza-escuro;
    border-radius: 25px;
    padding: 0 15px;
    font-size: 16px;
    width: 100%;
    height: 100%;
    outline: none;

    &::placeholder {
      color: $cinza-medio;
    }
  }

  .iconClear {
    position: absolute;
    display: none;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;

    &.active {
      display: block;
    }
  }
}
</style>
