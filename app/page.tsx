// app/page.tsx
export default function Home() {
  // A simple empty server action
  async function testAction() {
    'use server';
    console.log("Action invoked");
  }

  return (
    <main style={{ padding: '50px', fontFamily: 'sans-serif' }}>
      <h1>React2Shell (CVE-2025-55182) POC</h1>
      <p>
        This form connects to a Server Action. 
        Click the button, then check your Network tab to find the 
        <strong>Next-Action</strong> ID.
      </p>
      
      <form action={testAction}>
        <button type="submit" style={{ padding: '10px 20px', cursor: 'pointer' }}>
          Invoke Server Action
        </button>
      </form>
    </main>
  );
}
