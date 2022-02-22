<template>
  <div class="demo-control-panel">
    <input type="checkbox" v-model="configs.view.panEnabled"/>Pan enabled
    <input type="checkbox" v-model="configs.view.zoomEnabled"/>Zoom enabled
    <input type="checkbox" v-model="configs.node.draggable"/>Node draggable
  </div>
  <v-network-graph
  :nodes="nodes"
  :edges="edges"
  :layouts="layouts"
  :configs="configs"
  style="border:2px solid black; height: 500px;"
  />
</template>
<script>
  import { reactive } from "vue"
  import * as vNG from "v-network-graph"
  import data from '../data/data.json'

  export default {
    name: "Network",
    components: {},
    data() {
      return {
       nodes : data.nodes,
       edges : data.edges,
       layouts : data.layouts,
       configs : reactive(
        vNG.defineConfigs({
          view: {
            panEnabled: true,
            zoomEnabled: true,
            fit: true
          },
          node: {
            draggable: true,
          },
        })
        )
     }
   }
  }

</script>