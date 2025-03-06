<script>
  import Li from "./Li.svelte";

  export let config;
</script>

<style lang="postcss">
  footer {
    position: fixed;
    height: var(--heightMenu);
    max-width: 100vw;
    width: 100%;
    left: 0;
    bottom: 0;
    text-align: center;
    z-index: 1;
    background-color: var(--white);
    @media (min-width: 800px) {
      display: none;
    }
  }

  nav {
    display: flex;
    width: 100%;
    box-shadow: 0 0 var(--heightMenu) 0 var(--whiteDark);
  }

  ul {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;

    @media (min-width: 800px) {
      flex-direction: row;
      align-items: flex-start;
    }
  }
</style>

<div class="comodin mobile" />

<footer class="mobile">
  <nav>
    <ul>
      {#each config.Links as link}
        <Li link={link.link} text={link.text} />
      {/each}
    </ul>
  </nav>
</footer>
