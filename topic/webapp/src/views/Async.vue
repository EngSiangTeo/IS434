<template>
  <Suspense>
    <template #default>
      <AsyncNetworkGraph />
    </template>
    <template #fallback>
      <span>Loading...</span>
    </template>
  </Suspense>
</template>

<script>
import AsyncNetworkGraph from '../components/AsyncNetworkGraph.vue'
export default {
  name: 'Async',
  components: {
    AsyncNetworkGraph,
  },
}
</script>