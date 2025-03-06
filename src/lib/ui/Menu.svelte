<script>
  import Brand from "./Brand.svelte";
  import Li from "./Li.svelte";
  export let config;
  export let segment;

  let length = config.Links.length;
</script>

<style lang="postcss">
  aside {
    height: max-content;
    position: sticky;
    display: flex;
    flex-direction: row;
    top: 0;
    align-items: center;
    width: 100%;
    max-width: var(--maxwidth);
    justify-content: center;
    /* FONDO DEL MENU*/
    background-color: var(--white);

    @media (min-width: 800px) {
      justify-content: space-between;
    }
  }

  nav {
    display: none;
    font-weight: 400;

    @media (min-width: 800px) {
      display: flex;
      align-items: center;
      width: min-content;
      flex-direction: row-reverse;
      min-width: 25%;

      &.todo {
        width: 50%;
      }

      &.casi {
        width: 40%;
      }
    }
  }

  ul {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;
    font-weight: 400;

    @media (--medium) {
      flex-direction: row;
      align-items: flex-start;
    }
  }
  p {
    font-size: 120%;
  }
</style>

<aside>
  <Brand>
    <p>Brand</p>
  </Brand>
  <nav class={length >= 4 ? "todo" : "casi"}>
    <ul>
      {#each config.Links as link}
        <Li {segment} link={link.link} text={link.text} />
      {/each}
    </ul>
  </nav>
</aside>
