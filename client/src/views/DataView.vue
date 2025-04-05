<template>
    <div>
      <h1>Data</h1>
      <TicketSales />
    </div>
</template>

<script>
import TicketSales from '@/components/graphs/TicketSales.vue'

export default {
	name: "DataView",
  // computed: {
  //   ...mapGetters("datapage", [
  //     "hideInjuryGraph",
  //   ]),
  // },
	components: {
    TicketSales,
  },
};
</script>

<style scoped>

</style>