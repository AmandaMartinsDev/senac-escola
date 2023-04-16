<template>
  <div
    class="select-container"
    :style="{ width: width }"
    @click="isOpen = !isOpen"
    @mouseenter="mouseOver = true"
    @mouseleave="mouseOver = false"
  >
    <input
      type="text"
      :placeholder="input.placeholder"
      :value="value"
      @keyup="($event) => onKeyUp($event)"
      :readonly="!searchable"
      :class="{ active: isOpen }"
      @blur="close()"
    />
    <img
      :class="{ active: isOpen, icon: true }"
      src="../../assets/dropdown-icon.svg"
    />
    <img
      :class="{ active: value.trim() && mouseOver, iconClear: true }"
      src="../../assets/cross.svg"
      @click="clear($event)"
    />
    <ul :class="{ expanded: isOpen, collapsed: !isOpen }">
      <li v-for="option in listOptions" @click="onSelect(option)">
        {{ option.label }}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
class Input {
  placeholder: string = "";
  value: string = "";
  constructor(placeholder: string, value: string) {
    this.placeholder = placeholder;
    this.value = value;
  }
}
interface Option {
  value: string;
  label: string;
}
export default {
  props: {
    input: {
      type: Input,
      default: {
        placeholder: "Selecione",
        value: "",
      },
    },
    width: {
      type: String,
      default: "100%",
    },
    searchable: {
      type: Boolean,
      default: true,
    },
    options: {
      type: Array,
      default: [],
    },
    optionModel: {
      type: Object as () => Option,
      default: {
        value: "value",
        label: "label",
      },
    },
  },
  data() {
    return {
      isOpen: false,
      mouseOver: false,
      value: "",
      listOptions: this.options.map((option: any) => {
        return {
          value: option[this.optionModel.value],
          label: option[this.optionModel.label],
        };
      }) as Option[],
    };
  },
  computed: {
    getOptions() {
      let options = this.mappedOptions(this.options);
      this.listOptions = options;
    },
  },

  methods: {
    mappedOptions(list: any[]) {
      return list.map((option: any) => {
        return {
          value: option[this.optionModel.value],
          label: option[this.optionModel.label],
        };
      }) as Option[];
    },
    onSelect(option: Option) {
      this.value = option.label;
      this.$emit("onSelect", option);
    },
    onKeyUp(event: any) {
      let value = event.target.value;
      this.value = value;
      if (value.trim() === "") {
        this.listOptions = this.mappedOptions(this.options);
        return;
      }
      let options = this.options.filter((option: any) => {
        return option[this.optionModel.label]
          .toLowerCase()
          .includes(value.toLowerCase());
      });
      this.listOptions = this.mappedOptions(options);
    },
    clear(event: any) {
      event.stopPropagation();
      this.onSelect({ value: "", label: "" });
      this.listOptions = this.mappedOptions(this.options);
    },
    close() {
      setTimeout(() => {
        this.isOpen = false;
      }, 100);
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../styles/scss/variables.scss";
.select-container {
  position: relative;
  height: $base-height;
  display: flex;
  align-items: center;
  flex-direction: column;
  input {
    background: $branco;
    border: 1px solid $cinza-claro;
    color: $cinza-escuro;
    border-radius: 25px;
    width: 100%;
    padding: 0 15px;
    font-size: 16px;
    height: 50px;
    outline: none;

    &.active {
      border-bottom-left-radius: 0;
      border-bottom-right-radius: 0;
    }

    &::placeholder {
      color: $cinza-medio;
    }
  }

  .iconClear {
    position: absolute;
    display: none;
    right: 45px;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    z-index: 1000;

    &.active {
      display: block;
    }
  }

  .icon {
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    width: 20px;
    height: 20px;
    transition: all 0.2s ease-in-out;
    &.active {
      transform: translateY(-50%) rotate(180deg);
    }
  }

  ul {
    &.collapsed {
      display: none;
    }
    &.expanded {
      display: block;
    }
    position: absolute;
    top: 50px;
    list-style: none;
    padding: 0;
    margin: 0;
    background-color: $branco;
    width: 100%;
    border-bottom-left-radius: 25px;
    border-bottom-right-radius: 25px;
    overflow-x: hidden;
    z-index: 100;
    li {
      text-align: start;
      padding: 10px 15px;
      font-size: 16px;
      color: $cinza-escuro;
      cursor: pointer;
      &:hover {
        background-color: $cinza-claro;
      }
    }
  }
}
</style>
