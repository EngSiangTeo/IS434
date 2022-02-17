<template>
  <!-- <pre>{{ data.nodes }}</pre> -->
  <v-network-graph
    :nodes="data.nodes"
    :edges="data.edges"
    :layouts="data.layouts"
    :configs="configs"
    ref="graph"
    style="border: 1px solid red; height: 500px;"
  />
</template>

<script>
import { ref, reactive } from 'vue'
import * as vNG from "v-network-graph"

export default {
  name: 'AsyncNetworkGraph',
  async setup() {
    const data = ref(null)
    await new Promise((r) => setTimeout(r, 2000))
    try {
      const res = await fetch(process.env.VUE_APP_BE_SERVER_HOST + "/")
      data.value = await res.json()
      console.log(data)
    } catch (e) {
      console.error(e)
    }
    return { data }
  },
  data() {
    return {
      configs : reactive(
        vNG.defineConfigs({
          view: {
            panEnabled: false,
            zoomEnabled: true,
            fit: true
          },
          node: {
            draggable: true,
          },
        })
      )
    }
  },
}
</script>