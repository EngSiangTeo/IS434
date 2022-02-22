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
      <AsyncNetworkGraph :key="componentKey" :currentColours="c_index" :type="type"/>
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
      colours: ["red", "green", "blue", "yellow"],
      c_index: [0,1,2,3],
      componentKey: 0,
      type: "degree"
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