<template>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li v-for="(breadcrumb, index) in breadcrumbs" :key="index" class="breadcrumb-item">
          <router-link :to="breadcrumb.route">{{ breadcrumb.label }}</router-link>
        </li>
      </ol>
    </nav>
  </template>
  
  <script>
  export default {
    name: "Breadcrumbs",
    computed: {
      breadcrumbs() {
        const routes = this.$route.matched;
        return routes.map(route => ({
          label: route.meta.breadcrumb || route.name,
          route: route.path
        }));
      }
    }
  };
  </script>
  
  <style>
  /* Add your custom styling for breadcrumbs here */
  </style>