const basePath = import.meta.env.BASE_URL;

export function withBase(path: string): string {
  if (!path) {
    return basePath || '/';
  }

  if (/^(https?:|mailto:|#)/.test(path)) {
    return path;
  }

  const normalizedBase = basePath.endsWith('/') ? basePath.slice(0, -1) : basePath;
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;

  if (normalizedPath === '/') {
    return normalizedBase || '/';
  }

  return `${normalizedBase}${normalizedPath}`;
}
