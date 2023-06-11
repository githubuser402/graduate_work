<script setup>
</script>

<template>
  <header>

    <div class="wrapper">

      <nav>
        <!-- <RouterLink to="/">Home</RouterLink> -->
        <!-- <p>{{ this.$store.getters.count }}3e3</p> -->
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
body {
  height: 100%;
  background: #ebf4f5;
  background: linear-gradient(90deg, #ebf4f5 0%, #b5c6e0  100%);
  background: -moz-linear-gradient(90deg, #ebf4f5 0%, #b5c6e0  100%);
  background: -webkit-linear-gradient(90deg, #ebf4f5 0%, #b5c6e0 100%);
  filter: progid: DXImageTransform.Microsoft.gradient(startColorstr="#F86CA7", endColorstr="#F4D444", GradientType=1);
}
</style>
