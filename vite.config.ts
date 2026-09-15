import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
export default defineConfig({
  base: "./",
  plugins: [tailwindcss()],
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.endsWith("/questions.json")) return "question-bank";
          if (id.includes("node_modules")) return "vendor";
        },
      },
    },
  },
});
