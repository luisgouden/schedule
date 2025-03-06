<script>
  export let segment;
  export let link;
  export let text;
</script>

<style lang="postcss">
  li {
    padding: 0;
    font-size: 120%;

    @media (min-width: 800px) {
      font-size: 100%;
    }
  }

  .selected {
    color: purple;
  }
</style>

<li>
  <a class={segment === { link } ? "selected" : ""} href={link}> {text} </a>
</li>
