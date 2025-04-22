<template>
    <div>
      <div ref="repeatCustomerGraph"></div>
    </div>
</template>

<script>
// import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "AgeGraph",
  computed: {
    ...mapGetters("datapage", [
      "repeatCustomersData",
    ]),
  },
}

</script>