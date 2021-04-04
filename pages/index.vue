<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <menu-card />
    </v-col>
  </v-row>
</template>

<script>
import MenuCard from '~/components/MenuCard.vue'

export default {
  components: {
    MenuCard
  },
}
</script>
