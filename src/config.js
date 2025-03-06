
let Links = [
  { link: '.', text: 'blog' },
  { link: '.', text: 'shop' },
  { link: '.', text: 'about me' }
];

//cambiar tambien en app.html
let Layout = 'column';

let Landing = true;

if (Landing == true) {
  Layout = 'column';
};

const Config = {
  Links,
  Layout,
  Landing
};

export default Config;