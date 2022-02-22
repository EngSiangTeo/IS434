<template>
  <div v-for="(color, index) in colours" v-bind:key="color">
    <input type="checkbox" @change="filterColor(index,$event)" checked="checked"> {{color}}
  </div>
  <button @click="flip('degree')">Degree</button>
  <button @click="flip('eigenvector')">Eigenvector</button>
  <button @click="flip('betweeness')">Betweeness</button>
  <br/>
  <Suspense>
    <template #default>
      <AsyncNetworkGraph :key="componentKey" :currentColours="c_index" :type="type" :data="data"/>
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
  data(){
    return {
      colours: [],
      c_index: [],
      componentKey: 0,
      type: "degree",
      data: Object
    }
  },
  async created(){
    try {
      const res = await fetch(process.env.VUE_APP_BE_SERVER_HOST + "/")
      this.data = await res.json()
      console.log(this.data)
      this.colours = this.data.colours
      this.c_index = this.data.c_index
    } catch (e) {
      console.error(e)
    }
  },
  methods: {
    filterColor: function(index, event){
      this.componentKey =! this.componentKey
      if(event.target.checked){
        this.c_index.push(index)
      }else{
        this.c_index = this.c_index.filter(c => c != index)
      }
      console.log(this.c_index)
    },
    flip : function(type){
      this.componentKey =! this.componentKey
      this.type = type
    },
  }
}
</script>