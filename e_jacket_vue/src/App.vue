<template>
 <div class="wrapper">
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <router-link to="/" class="text"><h3>Djacket</h3></router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
        <li class="nav-item me-3">
          <router-link to="/summer" class="text">Summer</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/winter" class="text me-3">Winter</router-link>
        </li>
        <!-- <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li> -->
        <li class="nav-item">
          <router-link to="" class="btn btn-primary me-3">Login</router-link>
        </li>
        <li class="nav-item">
          <router-link to="" class="btn btn-info me-3">Cart</router-link>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>

<section>
  <router-view/>
</section>

<div class="footer">
  <footer>
    <center><p>copyright (c) 2022</p></center>
  </footer>
</div>
  
 </div>
  
</template>

<script>
  export default{
    
  }
</script>

<style> 
@import '../node_modules/bulma';

.text{
  text-decoration: none;
  color: white;
 }
 .text:hover{
  color: white;
 }
</style>
