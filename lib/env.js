const path = require('path');
const { getRoot } = require('bindings');

if (process.platform === 'win32') {
  let root = getRoot(__filename);
  let arch = process.arch === 'x64' ? '64' : '32';
  let envpath = path.join(root, `ctp_api/lib/win${arch}`);
  console.log(envpath)
  if (process.env.PATH.indexOf(envpath) === -1) {
    process.env.PATH += `;${envpath}`;
  }
}
