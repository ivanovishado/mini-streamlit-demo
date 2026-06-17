import type { DesignSystem, Page, SlideMeta, SlideTransition } from '@open-slide/core';
import { useSlidePageNumber } from '@open-slide/core';

export const design: DesignSystem = {
  palette: { bg: '#202945', text: '#ffffff', accent: '#FDCF85' },
  fonts: {
    display: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    body: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
  },
  typeScale: { hero: 152, body: 36 },
  radius: 8,
};

const muted = '#d8dee9';
const panel = '#17213a';
const crestRed = '#B12028';
const olive = '#8F993E';
const gray = '#404041';
const ink = '#000000';
const gdgBlue = '#4285f4';
const gdgGreen = '#0f9d58';
const gdgYellow = '#fbbc04';
const gdgRed = '#ea4335';

const EASE_OUT = 'cubic-bezier(0, 0, 0.2, 1)';
const EASE_IN = 'cubic-bezier(0.4, 0, 1, 1)';

const STYLE_ID = 'streamlit-workshop-styles';
if (typeof document !== 'undefined' && !document.getElementById(STYLE_ID)) {
  const style = document.createElement('style');
  style.id = STYLE_ID;
  style.textContent = `
    @keyframes osd-fade-up {
      from { opacity: 0; transform: translateY(18px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .osd-fade-up { animation: osd-fade-up 500ms cubic-bezier(0, 0, 0.2, 1) both; }
    .osd-code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      background: ${panel};
      color: var(--osd-accent);
      padding: 4px 12px;
      border-radius: 6px;
      font-size: 0.9em;
    }
  `;
  document.head.appendChild(style);
}

const Title = ({ children }: { children: React.ReactNode }) => (
  <h1
    style={{
      fontFamily: 'var(--osd-font-display)',
      fontSize: 'var(--osd-size-hero)',
      fontWeight: 900,
      lineHeight: 1.02,
      letterSpacing: 0,
      margin: 0,
      maxWidth: 1320,
      color: 'var(--osd-text)',
    }}
  >
    {children}
  </h1>
);

const Footer = () => {
  const { current, total } = useSlidePageNumber();
  return (
    <div
      style={{
        position: 'absolute',
        left: 112,
        right: 112,
        bottom: 54,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        fontFamily: 'var(--osd-font-body)',
        fontSize: 24,
        fontWeight: 700,
        letterSpacing: 1.6,
        color: muted,
        textTransform: 'uppercase',
      }}
    >
      <span>UdeG x GDG · Streamlit Workshop</span>
      <span style={{ color: 'var(--osd-accent)' }}>
        {String(current).padStart(2, '0')} / {String(total).padStart(2, '0')}
      </span>
    </div>
  );
};

const Eyebrow = ({ children }: { children: React.ReactNode }) => (
  <div
    style={{
      display: 'inline-flex',
      alignItems: 'center',
      gap: 14,
      fontFamily: 'var(--osd-font-body)',
      fontSize: 24,
      fontWeight: 800,
      letterSpacing: 3.6,
      color: 'var(--osd-accent)',
      textTransform: 'uppercase',
    }}
  >
    <span style={{ width: 72, height: 8, background: gdgBlue, borderRadius: 999 }} />
    <span>{children}</span>
  </div>
);

const ColorRail = () => (
  <div style={{ display: 'flex', gap: 16 }}>
    <span style={{ width: 86, height: 12, background: gdgBlue, borderRadius: 999 }} />
    <span style={{ width: 86, height: 12, background: gdgRed, borderRadius: 999 }} />
    <span style={{ width: 86, height: 12, background: gdgYellow, borderRadius: 999 }} />
    <span style={{ width: 86, height: 12, background: gdgGreen, borderRadius: 999 }} />
  </div>
);

const Frame = ({ children }: { children: React.ReactNode }) => (
  <section
    style={{
      width: '100%',
      height: '100%',
      position: 'relative',
      overflow: 'hidden',
      background: 'var(--osd-bg)',
      color: 'var(--osd-text)',
      fontFamily: 'var(--osd-font-body)',
    }}
  >
    <div style={{ position: 'absolute', left: 112, right: 112, top: 72, height: 4, background: 'var(--osd-accent)' }} />
    <div style={{ position: 'absolute', left: 112, top: 92 }}>
      <ColorRail />
    </div>
    <div
      style={{
        position: 'absolute',
        right: -160,
        bottom: -240,
        width: 620,
        height: 620,
        border: '34px solid var(--osd-accent)',
        borderRadius: 999,
        opacity: 0.18,
      }}
    />
    {children}
    <Footer />
  </section>
);

const ContentBlock = ({ children }: { children: React.ReactNode }) => (
  <div className="osd-fade-up" style={{ position: 'absolute', inset: '176px 112px 132px' }}>
    {children}
  </div>
);

const PageHeading = ({ children }: { children: React.ReactNode }) => (
  <h2
    style={{
      fontFamily: 'var(--osd-font-display)',
      fontSize: 76,
      lineHeight: 1.08,
      margin: '24px 0 40px',
      color: 'var(--osd-text)',
      maxWidth: 1320,
    }}
  >
    {children}
  </h2>
);

const BodyList = ({ children }: { children: React.ReactNode }) => (
  <ul
    style={{
      fontSize: 'var(--osd-size-body)',
      lineHeight: 1.55,
      color: muted,
      margin: 0,
      paddingLeft: 48,
      maxWidth: 1100,
    }}
  >
    {children}
  </ul>
);

const BodyText = ({ children, style }: { children: React.ReactNode; style?: React.CSSProperties }) => (
  <p
    style={{
      fontSize: 'var(--osd-size-body)',
      lineHeight: 1.55,
      color: muted,
      margin: 0,
      maxWidth: 980,
      ...style,
    }}
  >
    {children}
  </p>
);

const Code = ({ children }: { children: React.ReactNode }) => <span className="osd-code">{children}</span>;

const CheckItem = ({ children }: { children: React.ReactNode }) => (
  <li style={{ marginBottom: 28, display: 'flex', alignItems: 'flex-start', gap: 18 }}>
    <span style={{ color: 'var(--osd-accent)', fontWeight: 800 }}>✓</span>
    <span>{children}</span>
  </li>
);

const NumberedStep = ({ number, children }: { number: number; children: React.ReactNode }) => (
  <div style={{ display: 'flex', alignItems: 'flex-start', gap: 24, marginBottom: 28 }}>
    <span
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: 52,
        height: 52,
        borderRadius: '50%',
        background: 'var(--osd-accent)',
        color: ink,
        fontSize: 28,
        fontWeight: 900,
        flexShrink: 0,
      }}
    >
      {number}
    </span>
    <div style={{ fontSize: 'var(--osd-size-body)', lineHeight: 1.55, color: muted, paddingTop: 6 }}>{children}</div>
  </div>
);

const FlowCard = ({ label, desc }: { label: string; desc: string }) => (
  <div
    style={{
      background: panel,
      borderTop: '6px solid var(--osd-accent)',
      borderRadius: 'var(--osd-radius)',
      padding: 36,
    }}
  >
    <div style={{ fontSize: 40, fontWeight: 900, color: 'var(--osd-accent)', marginBottom: 16 }}>{label}</div>
    <div style={{ fontSize: 30, lineHeight: 1.45, color: muted }}>{desc}</div>
  </div>
);

const DatasetField = ({ col, q }: { col: string; q: string }) => (
  <div
    style={{
      background: panel,
      borderLeft: '8px solid ' + gdgBlue,
      borderRadius: 'var(--osd-radius)',
      padding: '28px 32px',
    }}
  >
    <Code>{col}</Code>
    <div style={{ fontSize: 30, color: muted, marginTop: 12 }}>{q}</div>
  </div>
);

const ShowCard = ({ fn, desc }: { fn: string; desc: string }) => (
  <div
    style={{
      background: panel,
      borderTop: '6px solid var(--osd-accent)',
      borderRadius: 'var(--osd-radius)',
      padding: 36,
    }}
  >
    <Code>{fn}</Code>
    <div style={{ fontSize: 30, lineHeight: 1.45, color: muted, marginTop: 16 }}>{desc}</div>
  </div>
);

const Cover: Page = () => (
  <Frame>
    <div className="osd-fade-up" style={{ position: 'absolute', left: 112, top: 226, width: 1240 }}>
      <Eyebrow>Taller UdeG x GDG</Eyebrow>
      <Title>Streamlit</Title>
      <p
        style={{
          fontSize: 52,
          lineHeight: 1.25,
          color: muted,
          maxWidth: 1100,
          margin: '34px 0 0',
        }}
      >
        De análisis de datos a web app local
      </p>
      <p style={{ fontSize: 28, color: muted, marginTop: 48, maxWidth: 900 }}>
        4 horas · 2 días · Cada estudiante construye su propio dashboard interactivo
      </p>
    </div>
    <div style={{ position: 'absolute', right: 112, top: 260 }}>
      <div
        style={{
          width: 520,
          height: 520,
          borderRadius: '50%',
          border: '24px solid var(--osd-accent)',
          opacity: 0.22,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <div
          style={{
            width: 360,
            height: 360,
            borderRadius: '50%',
            background: panel,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontFamily: 'ui-monospace, monospace',
            fontSize: 96,
            color: 'var(--osd-accent)',
            fontWeight: 800,
          }}
        >
          {'<> '}
        </div>
      </div>
    </div>
    <div style={{ position: 'absolute', left: 112, bottom: 154, width: 420, height: 18, background: crestRed }} />
  </Frame>
);

const PromisePage: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>El objetivo del taller</Eyebrow>
      <PageHeading>Al finalizar, cada uno de ustedes tendrá un dashboard local filtrable</PageHeading>
      <BodyList>
        <li style={{ marginBottom: 28 }}>
          Construirás una app funcional en <Code>localhost</Code> desde cero.
        </li>
        <li style={{ marginBottom: 28 }}>
          Conectarás controles a tu dataset <Code>data/estudiantes_ai.csv</Code>.
        </li>
        <li>Serás capaz de explicar tu app en 60 segundos.</li>
      </BodyList>
    </ContentBlock>
  </Frame>
);

const TwoDayMap: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Mapa de dos días</Eyebrow>
      <PageHeading>Día 1 construye la UI; Día 2 conecta los datos</PageHeading>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 64, marginTop: 8 }}>
        <div
          style={{
            background: panel,
            border: '4px solid var(--osd-accent)',
            borderRadius: 'var(--osd-radius)',
            padding: 44,
          }}
        >
          <div style={{ fontSize: 28, fontWeight: 800, color: 'var(--osd-accent)', marginBottom: 24 }}>DÍA 1</div>
          <ul style={{ fontSize: 32, lineHeight: 1.5, color: muted, margin: 0, paddingLeft: 32 }}>
            <li style={{ marginBottom: 16 }}>Setup del entorno</li>
            <li style={{ marginBottom: 16 }}>Modelo mental de Streamlit</li>
            <li>Widgets como variables</li>
          </ul>
        </div>
        <div
          style={{
            background: panel,
            border: '4px solid ' + gdgBlue,
            borderRadius: 'var(--osd-radius)',
            padding: 44,
          }}
        >
          <div style={{ fontSize: 28, fontWeight: 800, color: gdgBlue, marginBottom: 24 }}>DÍA 2</div>
          <ul style={{ fontSize: 32, lineHeight: 1.5, color: muted, margin: 0, paddingLeft: 32 }}>
            <li style={{ marginBottom: 16 }}>Filtros con Pandas</li>
            <li style={{ marginBottom: 16 }}>Dashboard completo</li>
            <li>Vista previa de despliegue</li>
          </ul>
        </div>
      </div>
    </ContentBlock>
  </Frame>
);

const Setup: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Setup</Eyebrow>
      <PageHeading>Antes de empezar</PageHeading>
      <div style={{ maxWidth: 1100 }}>
        <NumberedStep number={1}>
          Activa tu entorno virtual: <Code>source venv/bin/activate</Code>
        </NumberedStep>
        <NumberedStep number={2}>
          Instala dependencias: <Code>pip install -r requirements.txt</Code>
        </NumberedStep>
        <NumberedStep number={3}>
          Lanza la app: <Code>streamlit run streamlit_app.py</Code>
        </NumberedStep>
      </div>
    </ContentBlock>
  </Frame>
);

const WhatIsStreamlit: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Concepto</Eyebrow>
      <PageHeading>¿Qué es Streamlit?</PageHeading>
      <BodyList>
        <li style={{ marginBottom: 28 }}>
          Un script de Python que se convierte en lienzo de app web.
        </li>
        <li style={{ marginBottom: 28 }}>
          Cada línea se renderiza de arriba hacia abajo en el navegador.
        </li>
        <li>No necesitas HTML, CSS ni JavaScript para empezar.</li>
      </BodyList>
    </ContentBlock>
  </Frame>
);

const MentalModel: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Modelo mental</Eyebrow>
      <PageHeading>El script se actualiza completo</PageHeading>
      <BodyList>
        <li style={{ marginBottom: 28 }}>
          Streamlit ejecuta el archivo de arriba hacia abajo.
        </li>
        <li style={{ marginBottom: 28 }}>
          Cada cambio de código o interacción dispara un nuevo rerun.
        </li>
        <li>Los widgets son variables Python: su valor cambia y el resto del script responde.</li>
      </BodyList>
    </ContentBlock>
  </Frame>
);

const FirstAppCheckpoint: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Checkpoint</Eyebrow>
      <PageHeading>Tu primera app</PageHeading>
      <BodyText>Abre <Code>exercises/day1/01_first_app.py</Code> y completa el objetivo:</BodyText>
      <div
        style={{
          background: panel,
          border: '4px solid var(--osd-accent)',
          borderRadius: 'var(--osd-radius)',
          padding: 36,
          marginTop: 36,
          maxWidth: 1100,
        }}
      >
        <div style={{ fontSize: 28, fontWeight: 800, color: 'var(--osd-accent)', marginBottom: 16 }}>META</div>
        <div style={{ fontSize: 32, lineHeight: 1.5, color: 'var(--osd-text)' }}>
          Escribir <Code>st.title("Mi primera app")</Code> y mostrar un texto con <Code>st.write</Code>.
        </div>
      </div>
      <BodyText style={{ marginTop: 36 }}>
        <strong style={{ color: 'var(--osd-text)' }}>Debrief:</strong> ¿qué pasó en el navegador al guardar el archivo?
      </BodyText>
    </ContentBlock>
  </Frame>
);

const TextPrimitives: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Primitivas</Eyebrow>
      <PageHeading>Texto y retroalimentación</PageHeading>
      <BodyList>
        <li style={{ marginBottom: 28 }}>
          Estructura: <Code>st.title</Code>, <Code>st.header</Code>, <Code>st.markdown</Code>, <Code>st.write</Code>.
        </li>
        <li style={{ marginBottom: 28 }}>
          Mensajes de estado: <Code>st.success</Code>, <Code>st.info</Code>, <Code>st.warning</Code>, <Code>st.error</Code>.
        </li>
        <li>Úsalos para guiar al usuario y validar resultados.</li>
      </BodyList>
    </ContentBlock>
  </Frame>
);

const WidgetsAsVariables: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Widgets</Eyebrow>
      <PageHeading>Los widgets son variables</PageHeading>
      <BodyList>
        <li style={{ marginBottom: 28 }}>
          <Code>st.button</Code>, <Code>st.slider</Code> y <Code>st.selectbox</Code> retornan valores.
        </li>
        <li style={{ marginBottom: 28 }}>
          Guarda el valor en una variable y úsalo después como cualquier otra de Python.
        </li>
        <li>Si el usuario interactúa, el script se rerun y la variable se actualiza.</li>
      </BodyList>
    </ContentBlock>
  </Frame>
);

const WidgetCheckpoint: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Checkpoint</Eyebrow>
      <PageHeading>Prueba un widget</PageHeading>
      <BodyText>Abre <Code>exercises/day1/02_widgets.py</Code>:</BodyText>
      <div
        style={{
          background: panel,
          border: '4px solid ' + gdgBlue,
          borderRadius: 'var(--osd-radius)',
          padding: 36,
          marginTop: 36,
          maxWidth: 1100,
        }}
      >
        <div style={{ fontSize: 28, fontWeight: 800, color: gdgBlue, marginBottom: 16 }}>META</div>
        <div style={{ fontSize: 32, lineHeight: 1.5, color: 'var(--osd-text)' }}>
          Lee un <Code>st.slider</Code> y muestra su valor con <Code>st.write</Code>.
        </div>
      </div>
      <BodyText style={{ marginTop: 36 }}>
        <strong style={{ color: 'var(--osd-text)' }}>Debrief:</strong> ¿cómo cambia el número al mover el control?
      </BodyText>
    </ContentBlock>
  </Frame>
);

const DayOneCheckpoint: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Cierre día 1</Eyebrow>
      <PageHeading>Widget → Variable → Output</PageHeading>
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: 32,
          marginTop: 24,
          maxWidth: 1200,
        }}
      >
        <FlowCard label="Widget" desc="El usuario interactúa." />
        <FlowCard label="Variable" desc="Python guarda el valor." />
        <FlowCard label="Output" desc="Streamlit redibuja." />
      </div>
    </ContentBlock>
  </Frame>
);

const DayTwoDivider: Page = () => (
  <Frame>
    <div className="osd-fade-up" style={{ position: 'absolute', inset: '176px 112px 132px', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
      <Eyebrow>Día 2</Eyebrow>
      <Title>De Pandas a dashboard</Title>
      <p style={{ fontSize: 44, lineHeight: 1.4, color: muted, maxWidth: 980, marginTop: 34 }}>
        Conecta análisis de datos con controles interactivos.
      </p>
    </div>
  </Frame>
);

const DatasetMap: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Datos</Eyebrow>
      <PageHeading>El dataset estudiantes_ai.csv</PageHeading>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 32, maxWidth: 1200, marginTop: 8 }}>
        <DatasetField col="nombre" q="¿Quién es el estudiante?" />
        <DatasetField col="carrera" q="¿A qué programa pertenece?" />
        <DatasetField col="semestre" q="¿Qué tan avanzado está?" />
        <DatasetField col="interes_ia" q="¿Le interesa la inteligencia artificial?" />
      </div>
    </ContentBlock>
  </Frame>
);

const FilterPattern: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Patrón</Eyebrow>
      <PageHeading>Input → Condición → DataFrame filtrado</PageHeading>
      <div
        style={{
          background: ink,
          borderRadius: 'var(--osd-radius)',
          padding: 44,
          marginTop: 24,
          maxWidth: 1100,
          fontFamily: 'ui-monospace, monospace',
          fontSize: 34,
          lineHeight: 1.7,
          color: 'var(--osd-text)',
        }}
      >
        <span style={{ color: gdgBlue }}>carrera</span> = st.selectbox(
        <br />
        &nbsp;&nbsp;<span style={{ color: gdgGreen }}>"Elige carrera"</span>, df[<span style={{ color: gdgYellow }}>"carrera"</span>].unique()
        <br />)
        <br />
        <span style={{ color: muted }}>filtrado</span> = df[df[<span style={{ color: gdgYellow }}>"carrera"</span>] == carrera]
        <br />
        st.dataframe(filtrado)
      </div>
    </ContentBlock>
  </Frame>
);

const PandasFilterCheckpoint: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Checkpoint</Eyebrow>
      <PageHeading>Filtra con Pandas</PageHeading>
      <BodyText>Abre <Code>exercises/day2/01_pandas_filters.py</Code>:</BodyText>
      <div
        style={{
          background: panel,
          border: '4px solid ' + gdgGreen,
          borderRadius: 'var(--osd-radius)',
          padding: 36,
          marginTop: 36,
          maxWidth: 1100,
        }}
      >
        <div style={{ fontSize: 28, fontWeight: 800, color: gdgGreen, marginBottom: 16 }}>META</div>
        <div style={{ fontSize: 32, lineHeight: 1.5, color: 'var(--osd-text)' }}>
          Usa un <Code>selectbox</Code> para filtrar el DataFrame y mostrar solo las filas elegidas.
        </div>
      </div>
      <BodyText style={{ marginTop: 36 }}>
        <strong style={{ color: 'var(--osd-text)' }}>Debrief:</strong> ¿qué pasa si eliges otra opción?
      </BodyText>
    </ContentBlock>
  </Frame>
);

const ShowingData: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Visualización</Eyebrow>
      <PageHeading>Muestra datos de tres formas</PageHeading>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 32, marginTop: 24, maxWidth: 1200 }}>
        <ShowCard fn="st.dataframe" desc="Tabla interactiva." />
        <ShowCard fn="st.metric" desc="Un número clave grande." />
        <ShowCard fn="st.bar_chart" desc="Gráfica de barras rápida." />
      </div>
    </ContentBlock>
  </Frame>
);

const LayoutPage: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Layout</Eyebrow>
      <PageHeading>Organiza el dashboard</PageHeading>
      <BodyList>
        <li style={{ marginBottom: 28 }}>
          Filtros en la barra lateral con <Code>st.sidebar</Code>.
        </li>
        <li style={{ marginBottom: 28 }}>
          Resultados principales en el área central.
        </li>
        <li>KPIs en columnas con <Code>st.columns</Code> para mostrar varias métricas.</li>
      </BodyList>
    </ContentBlock>
  </Frame>
);

const ReferenceAppWalkthrough: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Mapa de referencia</Eyebrow>
      <PageHeading>Explora streamlit_app.py</PageHeading>
      <BodyList>
        <li style={{ marginBottom: 28 }}>
          Página de introducción con contexto del taller.
        </li>
        <li style={{ marginBottom: 28 }}>
          Página de componentes: widgets vistos en acción.
        </li>
        <li>Filtros y capstone: el dashboard que vas a replicar.</li>
      </BodyList>
    </ContentBlock>
  </Frame>
);

const CapstoneBuildPlan: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Proyecto final</Eyebrow>
      <PageHeading>Construye tu dashboard</PageHeading>
      <BodyText>Abre <Code>exercises/day2/02_capstone_starter.py</Code>:</BodyText>
      <div
        style={{
          background: panel,
          border: '4px solid ' + crestRed,
          borderRadius: 'var(--osd-radius)',
          padding: 36,
          marginTop: 36,
          maxWidth: 1100,
        }}
      >
        <div style={{ fontSize: 28, fontWeight: 800, color: crestRed, marginBottom: 16 }}>META</div>
        <div style={{ fontSize: 32, lineHeight: 1.5, color: 'var(--osd-text)' }}>
          Completa el dashboard: sidebar con filtros, métricas en columnas y gráfica de barras.
        </div>
      </div>
    </ContentBlock>
  </Frame>
);

const CapstoneSuccessCriteria: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Criterios de éxito</Eyebrow>
      <PageHeading>Tu dashboard debe cumplir</PageHeading>
      <div style={{ maxWidth: 1100 }}>
        <ul style={{ listStyle: 'none', padding: 0, margin: 0, fontSize: 'var(--osd-size-body)', lineHeight: 1.55, color: muted }}>
          <CheckItem>Los filtros actualizan la tabla.</CheckItem>
          <CheckItem>Las métricas cambian al filtrar.</CheckItem>
          <CheckItem>La gráfica refleja los datos filtrados.</CheckItem>
          <CheckItem>Se puede exportar o copiar la tabla resultante.</CheckItem>
        </ul>
      </div>
    </ContentBlock>
  </Frame>
);

const DeploymentPreview: Page = () => (
  <Frame>
    <ContentBlock>
      <Eyebrow>Despliegue</Eyebrow>
      <PageHeading>De local a la nube: conceptos</PageHeading>
      <BodyList>
        <li style={{ marginBottom: 28 }}>
          Subes tu repo a GitHub con <Code>requirements.txt</Code> completo.
        </li>
        <li style={{ marginBottom: 28 }}>
          Configuras secrets si tu app necesita credenciales.
        </li>
        <li>Streamlit Community Cloud ejecuta <Code>streamlit run app.py</Code> por ti.</li>
      </BodyList>
    </ContentBlock>
  </Frame>
);

const Closing: Page = () => (
  <Frame>
    <div className="osd-fade-up" style={{ position: 'absolute', inset: '176px 112px 132px', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
      <Eyebrow>Cierre</Eyebrow>
      <h2 style={{ fontFamily: 'var(--osd-font-display)', fontSize: 92, lineHeight: 1.08, margin: '24px 0 40px', maxWidth: 1320, color: 'var(--osd-text)' }}>Adapta, no reescribas</h2>
      <BodyList>
        <li style={{ marginBottom: 28 }}>
          Reemplaza los datos provisionales por los de la Semana 3.
        </li>
        <li style={{ marginBottom: 28 }}>
          Ajusta los filtros y métricas; la estructura del dashboard sigue igual.
        </li>
        <li>Gracias. ¿Preguntas?</li>
      </BodyList>
    </div>
    <div style={{ position: 'absolute', left: 112, bottom: 154, width: 380, height: 18, background: crestRed }} />
  </Frame>
);

export const transition: SlideTransition = {
  duration: 200,
  exit: {
    duration: 140,
    easing: EASE_IN,
    keyframes: [
      { opacity: 1, transform: 'translateY(0)' },
      { opacity: 0, transform: 'translateY(-4px)' },
    ],
  },
  enter: {
    duration: 200,
    delay: 80,
    easing: EASE_OUT,
    keyframes: [
      { opacity: 0, transform: 'translateY(6px)' },
      { opacity: 1, transform: 'translateY(0)' },
    ],
  },
};

export const meta: SlideMeta = {
  title: 'Streamlit: de análisis de datos a web app local',
  theme: 'udeg-gdg',
  createdAt: '2026-06-17T04:11:14.174Z',
};

export default [
  Cover,
  PromisePage,
  TwoDayMap,
  Setup,
  WhatIsStreamlit,
  MentalModel,
  FirstAppCheckpoint,
  TextPrimitives,
  WidgetsAsVariables,
  WidgetCheckpoint,
  DayOneCheckpoint,
  DayTwoDivider,
  DatasetMap,
  FilterPattern,
  PandasFilterCheckpoint,
  ShowingData,
  LayoutPage,
  ReferenceAppWalkthrough,
  CapstoneBuildPlan,
  CapstoneSuccessCriteria,
  DeploymentPreview,
  Closing,
] satisfies Page[];
