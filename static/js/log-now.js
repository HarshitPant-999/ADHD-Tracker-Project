document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("log-now-btn");
  const timestampField = document.getElementById("timestamp");

  if (!button || !timestampField) return; //scrap this function further 

  button.addEventListener("click", () => {
    const now = new Date();
    const pad = (number) => String(number).padStart(2, "0");
    const year = now.getFullYear();
    const month = pad(now.getMonth() + 1);
    const day = pad(now.getDate());
    const hours = pad(now.getHours());
    const minutes = pad(now.getMintes());

    timestampField.value = `${year}-${month}-${day}T${hours}:${minutes}`
    button.textContent = "Time set ✓";
    setTimeout(() => {
      button.textContent = "Use current time";
    }, 1200);
  });
});
