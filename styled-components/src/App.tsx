import React, { ReactNode } from 'react';
import styled from 'styled-components';


//styled-components utilities tagged template literals to style your components.
const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;

const Wrapper = styled.section`
  padding: 4em;
  background: papayawhip;
`

//Adapting based on props
const Button = styled.button<{primary?: boolean}>`
  background: ${props => props.primary ? "palevioletred" : "white"};
  color: ${props => props.primary ? "white" : "palevioletred"};
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
`;

//Extending styles
const TomatoButton = styled(Button)`
  color: tomato;
  border-color: tomato;
`;

//styling any component
//You can add styling to the specific child using '& >' or 'nth-child()'
const Link = ({ className, children }: {className?: string, children: ReactNode}) => (
  <a className={className}>
    {children}
  </a>
);

const StyledLink = styled(Link)`
  color: palevioletred;
  font-weight: bold;
`;

function App() {
  return (
    <>
      <Wrapper>
        <Title>
          Hello World!
        </Title>
      </Wrapper>
      <Button>Normal</Button>
      <Button primary>Primary</Button>
      <TomatoButton>Tomato Button</TomatoButton>
      <div>
        <Link>Unstyled, boring Link</Link>
        <br/>
        <StyledLink>Styled, existing Link</StyledLink>
      </div>
    </>
  );
}

export default App;
