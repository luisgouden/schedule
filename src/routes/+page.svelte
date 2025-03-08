<script>
  import schedule from "../schedule_3.js";

  const crono = 110;

  let session = [];
  let unique = {};
  let end;
  let ending;
  let remaining;
  let nextSessionStart;
  let now = new Date();
  $: hour = now.getHours();
  $: min = now.getMinutes();
  $: sec = now.getSeconds();
  function updateTime() {
    const intervalId = setInterval(() => {
      now = new Date();
      restart();
    }, 1000);

    // Cleanup interval on component unmount
    return () => clearInterval(intervalId);
  }

  function getSessionClass({ Start, Ends }) {
    const startTime = new Date(`${now.toDateString()} ${Start}`);
    const endTime = new Date(`${now.toDateString()} ${Ends}`);
    if (now < startTime) {
      return "future";
    } else if (now > endTime) {
      return "past";
    } else {
      return "active";
    }
  }

  function formatTime(time) {
    const hours = Math.floor(time / (1000 * 60 * 60))
      .toString()
      .padStart(2, "0");
    const minutes = Math.floor((time % (1000 * 60 * 60)) / (1000 * 60))
      .toString()
      .padStart(2, "0");
    const seconds = Math.floor((time % (1000 * 60)) / 1000)
      .toString()
      .padStart(2, "0");
    return `${hours}:${minutes}:${seconds}`;
  }

  function getBackgroundColor(time) {
    if (time > 10 * 60 * 1000) {
      return "white";
    } else if (time > 5 * 60 * 1000) {
      return "yellow";
    } else {
      return "red";
    }
  }

  function restart() {
    unique = {};
    const activeSession = schedule.find(
      (session) => getSessionClass(session) === "active",
    );
    end = activeSession ? activeSession.Ends : null;
    ending = new Date(`${now.toDateString()} ${end}`);
    remaining = end ? ending - now : null;

    if (!activeSession) {
      const futureSessions = schedule.filter(
        (session) => getSessionClass(session) === "future",
      );
      const nextSessionTeamEvent = futureSessions.find(
        (session) => session.Team === "Session",
      );

      if (nextSessionTeamEvent) {
        nextSessionStart = new Date(
          `${now.toDateString()} ${nextSessionTeamEvent.Start}`,
        );
      } else if (futureSessions.length > 0) {
        nextSessionStart = new Date(
          `${now.toDateString()} ${futureSessions[0].Start}`,
        );
      } else {
        nextSessionStart = null;
      }
    } else {
      nextSessionStart = null;
    }
  }

  updateTime();
</script>

<style>
  table {
    margin: 0 auto;
    border-collapse: collapse;
  }

  th,
  td {
    padding: 10px;
    border: 1px solid black;
  }
  .future {
    background-color: lightgreen;
  }

  .past {
    background-color: lightgray;
  }

  .active {
    background-color: yellow;
  }
  .session {
    font-weight: bold;
  }
  p {
    text-align: center;
    font-size: 2em;
  }
</style>

{#key unique}
  <p>
    {hour} : {min} : {sec}
  </p>

  <table>
    <thead>
      <tr>
        <th>Start</th>
        <th>End</th>
        <th>Event</th>
      </tr>
    </thead>
    <tbody>
      {#each schedule as session}
        <tr
          class={`${getSessionClass(session)} ${session.Team === "Session" ? "session" : ""}`}
        >
          <td>{session.Start}</td>
          <td>{session.Ends}</td>
          <td>{session.Event}</td>
        </tr>
      {/each}
    </tbody>
  </table>

  {#if end}
    <div style="background-color: {getBackgroundColor(remaining)}">
      <p>
        Tiempo restante: {formatTime(remaining)} / {Math.floor(
          remaining / (1000 * crono),
        )} vueltas
      </p>
    </div>
  {:else if nextSessionStart}
    <p>Tiempo para la próxima sesión: {formatTime(nextSessionStart - now)}</p>
  {:else}
    <p>No hay sesiones futuras</p>
  {/if}
{/key}
