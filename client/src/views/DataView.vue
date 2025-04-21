<template>
    <div>
      <h1>Data</h1>
      <div class="graph-area">
        <TicketSales />
        <AgeGraph />
        <RepeatCustomer />
      </div>
    </div>
</template>

<script>
import TicketSales from '@/components/graphs/TicketSales.vue'
import AgeGraph from '@/components/graphs/AgeGraph.vue'
import RepeatCustomer from '@/components/graphs/RepeatCustomer.vue'

export default {
	name: "DataView",
	components: {
    TicketSales,
    AgeGraph,
    RepeatCustomer,
  },
};
</script>

<style scoped>

.graph-area {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  border: 2px solid red; 
}

</style>