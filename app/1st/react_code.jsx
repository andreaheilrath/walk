'use strict';

// Example usage: <ShoppingList name="Mark" />

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'klick me!'
    );
  }
}

function tick() {
  const element = (
      "It is time." //{new Date().toLocaleTimeString()}.
  );
  // highlight-next-line
  ReactDOM.render(<p>Hello</p>, document.getElementById('root'));
}

setInterval(tick, 1000);


ReactDOM.render(<p>Hello</p>, document.getElementById('root'));

const domContainer2 = document.querySelector('#root2');
ReactDOM.render(e(LikeButton), domContainer2);
