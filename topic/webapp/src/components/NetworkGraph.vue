<template>
	<v-network-graph
    :nodes="nodes"
    :edges="edges"
    :layouts="layouts"
    style="border: 1px solid red; height: 500px;"
  />

</template>
<script>
export default {
  name: "NetworkGraph",
  components: {},
  props: {
      nodes: Object,
      edges: Object,
      layouts: Object
  }
};
</script>