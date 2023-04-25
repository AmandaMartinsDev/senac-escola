<template>
  <button
    :class="{
      neutral: neutral,
      danger: danger,
      primary: !danger,
      active: active,
      'text-centered': centered,
      between: iconSrc && text,
      center: iconSrc && !text,
    }"
    :style="{
      width: width,
    }"
    @click="$emit('onClick')"
  >
    <span>{{ text }}</span>
    <img class="icon" v-if="iconSrc" :src="iconSrc" />
  </button>
</template>

<script lang="ts">
export default {
  props: {
    text: {
      type: String,
      default: "",
    },
    danger: {
      type: Boolean,
      default: false,
    },
    active: {
      type: Boolean,
      default: false,
    },
    centered: {
      type: Boolean,
      default: false,
    },
    width: {
      type: String,
      default: "fit-content",
    },
    iconSrc: {
      type: String,
      default: "",
    },
    neutral: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../styles/scss/variables.scss";

button {
  height: $base-height;
  padding: 14px 28px 16px 28px;
  border-radius: 25px;
  border: none;
  font-size: 16px;
  font-family: "Noto Sans", sans-serif;
  text-align: start;
  cursor: pointer;
  display: flex;
  align-items: center;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.15);

  &.between {
    justify-content: space-between;
  }

  &.center {
    justify-content: center;
    padding: 16px;
  }

  &.text-centered {
    text-align: center;
  }
  &.primary {
    background: $azul-claro;
    &:hover,
    &.active {
      background: $azul;
    }
  }
  &.danger {
    background: $vermelho;
  }

  &.neutral {
    background: $branco;
    &:hover,
    &.active {
      background: $cinza-claro;
    }
  }

  .icon {
    width: 20px;
    height: 20px;
  }
}
</style>
