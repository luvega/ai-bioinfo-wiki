import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

const repository = process.env.GITHUB_REPOSITORY?.split('/')[1] ?? 'ai-bioinfo-wiki';
const owner = process.env.GITHUB_REPOSITORY?.split('/')[0] ?? 'luvega';
const githubPagesBase = `/${repository}`;
const githubPagesSite = `https://${owner}.github.io/${repository}`;

export default defineConfig({
  integrations: [mdx()],
  site: process.env.ASTRO_SITE ?? githubPagesSite,
  base: process.env.ASTRO_BASE ?? (process.env.GITHUB_ACTIONS ? githubPagesBase : '/'),
  markdown: {
    shikiConfig: {
      theme: 'github-light'
    }
  }
});
