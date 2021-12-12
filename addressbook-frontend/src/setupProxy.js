const { createProxyMiddleware }  = require("http-proxy-middleware");

module.exports = app => {
  app.use(
    "/api",
    createProxyMiddleware({
      target: "http://172.28.1.3:8000",
      changeOrigin: true
    })
  );
  app.use(
    "/garments",
    createProxyMiddleware({
      target: "http://172.28.1.3:8000",
      changeOrigin: true
    })
  );
};