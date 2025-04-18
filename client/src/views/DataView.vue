<template>
    <div>
      <h1>Data</h1>
      <div class="graph-area">
        <TicketSales />
        <AgeGraph />
      </div>
    </div>
</template>

<script>
import TicketSales from '@/components/graphs/TicketSales.vue'
import AgeGraph from '@/components/graphs/AgeGraph.vue'

export default {
	name: "DataView",
  // computed: {
  //   ...mapGetters("datapage", [
  //     "hideInjuryGraph",
  //   ]),
  // },
	components: {
    TicketSales,
    AgeGraph,
  },
};
</script>

<style scoped>

.graph-area {
  border: 2px solid red; 
}

</style>