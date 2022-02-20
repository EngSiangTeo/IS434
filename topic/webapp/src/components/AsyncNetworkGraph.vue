<template>
  <!-- <pre>{{ data.nodes }}</pre> -->
  <button @click="flip('degree')">Degree</button>
  <button @click="flip('eigenvector')">Eigenvector</button>
  <button @click="flip('betweeness')">Betweeness</button>
  <button @click="reset">Test</button>
  <v-network-graph
    :nodes="filterNodes"
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
      console.log(data.value)
    } catch (e) {
      console.error(e)
    }
    return { data }
  },
  data() {
    return {
      configs : this.setUpConfigs(),
      filterNodes: this.data.nodes,
    }
  },
  props: {
    currentColours: Object
  },
  created(){
    this.filterNode()
  },
  methods:{
    setUpConfigs : function(type="degree"){
      return reactive(
        vNG.defineConfigs({
          view: {
            panEnabled: true,
            zoomEnabled: true,
            fit: true
          },
          node: {
            normal: {
              type: "circle",
              radius: node => (type == "degree" ? node.size : (type == "eigenvector" ? node.e_size : node.b_size)),
              color: node => node.color,
              strokeWidth: 3,
              strokeColor: "black",
            },
            hover: {
              radius: node => (type == "degree" ? node.size : (type == "eigenvector" ? node.e_size : node.b_size)) + 2,
              color: node => node.color,
              strokeWidth: 3,
              strokeColor: "black",
            },
            selectable: true,
          },
        })
      )
    },
    flip : function(type){
      console.log(this.currentColours)
      this.configs = this.setUpConfigs(type)
    },
    filterNode: function(){
      var obj = {}
      for(var node of Object.entries({...this.data.nodes})){
        if(this.currentColours.includes(node[1].community)){
          obj[node[0]] = node[1]
        }
      }
      this.filterNodes = obj
    },
    reset : function(){
      this.filterNodes = this.data.nodes
    }
  }
}
</script>