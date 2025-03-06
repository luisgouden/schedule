<script>
  import "../app.postcss";

  import Menu from "$lib/ui/Menu.svelte";
  import LateralMenu from "$lib/ui/LateralMenu.svelte";
  import Footer from "$lib/ui/Footer.svelte";
  import config from "../config.js";

  export let segment;

  let layout = config.Layout;
</script>

<style>
</style>

{#if !config.Landing}
  {#if layout === "column"}
    <Menu {config} {segment} />
  {:else if layout === "row"}
    <LateralMenu {config} {segment} />
  {/if}
{/if}

<main>
  <slot />
</main>

{#if !config.Landing}
  <Footer {config} {segment} />
{/if}
