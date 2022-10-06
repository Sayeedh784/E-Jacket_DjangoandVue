<template>
  <div class="home">
    <section>
      <div class="container-fluid hero">
        <center>
          <h2>Welcome to Djacket</h2>
          <p>The best jacket store in online</p>
        </center>
      </div>
    </section>
    <div>
      <center class="mt-5 mb-5">
        <h1>Latest Products</h1>
      </center>
    </div>
    <section>
      <div class="container">
        <div class="row">
          
            <div class="col-md-4" v-for="product in latestProducts" v-bind:key="product.id">
              <div class="card">
                <img
                  :src="product.get_thumbnail"
                  class="card-img-top"
                  alt="..."
                />
                <div class="card-body">
                  <h5 class="card-title">{{ product.name }}</h5>
                  <p class="card-text">
                    {{ product.price }}$
                  </p>
                  View details
                </div>
              </div>
            
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    async getLatestProducts() {
     let result = await axios.get("http://127.0.0.1:8000/api/v1/latest-product/")
        console.warn(result)
        
          this.latestProducts = result.data;
        
    },
  },
};
</script>

<style>
.hero {
  background-color: rgb(38, 36, 36);
  padding: 100px 0 100px 0;
  color: white;
}
img{
  height: 300px;
  width: 100%;
}
</style>