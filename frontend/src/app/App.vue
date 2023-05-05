<template>
  <i-layout vertical class="app">
    <i-layout-aside :style="{display: currentRouteName == '/login'? 'none': 'flex'}">
      <Navbar></Navbar>
    </i-layout-aside>
    <i-layout-content>
      <router-view></router-view>
    </i-layout-content>
  </i-layout>
</template>

<script lang="ts">
import Navbar from "./components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
  computed: {
    currentRouteName() {
      return this.$route.path;
    },
  }
};
</script>

<style scoped lang="scss">
.app {
  height: 100vh !important;
}
</style>
