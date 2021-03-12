const { app, BrowserWindow } = require("electron");
const path = require("path");
const url = require("url");

let window;

const createBillManagementWindow = () => {
  window = new BrowserWindow();
  window.maximize();

  window.loadURL(
    url.format({
      pathname: path.join(__dirname, `/dist/index.html`),
      protocol: "file:",
      slashes: true,
    })
  );

  window.webContents.openDevTools();

  window.on("closed", () => {
    window = null;
  });
};

app.on("ready", createBillManagementWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", () => {
  if (window === null) createBillManagementWindow();
});

require("electron-reload")(__dirname, {
  electron: require(`${__dirname}/node_modules/electron`),
});
