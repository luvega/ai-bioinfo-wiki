const escapeHtml = (value: string) =>
  value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');

const inlineMarkdown = (value: string) =>
  escapeHtml(value)
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/`([^`]+)`/g, '<code>$1</code>');

export function renderSimpleMarkdown(markdown: string) {
  const text = markdown.replace(/^---[\s\S]*?---\s*/, '');
  const lines = text.split(/\r?\n/);
  const html: string[] = [];
  let paragraph: string[] = [];
  let listItems: string[] = [];
  let orderedItems: string[] = [];
  let codeLines: string[] = [];
  let codeLang = '';

  const flushParagraph = () => {
    if (!paragraph.length) return;
    html.push(`<p>${inlineMarkdown(paragraph.join(' '))}</p>`);
    paragraph = [];
  };

  const flushLists = () => {
    if (listItems.length) {
      html.push(`<ul>${listItems.map((item) => `<li>${inlineMarkdown(item)}</li>`).join('')}</ul>`);
      listItems = [];
    }
    if (orderedItems.length) {
      html.push(`<ol>${orderedItems.map((item) => `<li>${inlineMarkdown(item)}</li>`).join('')}</ol>`);
      orderedItems = [];
    }
  };

  const flushCode = () => {
    const langClass = codeLang ? ` language-${escapeHtml(codeLang)}` : '';
    const blockClass = codeLang === 'mermaid' ? ' mermaid-source' : '';
    html.push(`<pre class="code-block${blockClass}"><code class="${langClass.trim()}">${escapeHtml(codeLines.join('\n'))}</code></pre>`);
    codeLines = [];
    codeLang = '';
  };

  for (const rawLine of lines) {
    const line = rawLine.trimEnd();
    const trimmed = line.trim();

    if (codeLang || trimmed.startsWith('```')) {
      if (trimmed.startsWith('```')) {
        if (codeLang) {
          flushCode();
        } else {
          flushParagraph();
          flushLists();
          codeLang = trimmed.slice(3).trim() || 'text';
        }
      } else {
        codeLines.push(line);
      }
      continue;
    }

    if (!trimmed) {
      flushParagraph();
      flushLists();
      continue;
    }

    const heading = trimmed.match(/^(#{1,4})\s+(.+)$/);
    if (heading) {
      flushParagraph();
      flushLists();
      const level = Math.min(heading[1].length + 1, 5);
      html.push(`<h${level}>${inlineMarkdown(heading[2])}</h${level}>`);
      continue;
    }

    const bullet = trimmed.match(/^-\s+(.+)$/);
    if (bullet) {
      flushParagraph();
      orderedItems = [];
      listItems.push(bullet[1]);
      continue;
    }

    const ordered = trimmed.match(/^\d+\.\s+(.+)$/);
    if (ordered) {
      flushParagraph();
      listItems = [];
      orderedItems.push(ordered[1]);
      continue;
    }

    paragraph.push(trimmed);
  }

  flushParagraph();
  flushLists();
  if (codeLang) flushCode();
  return html.join('\n');
}
