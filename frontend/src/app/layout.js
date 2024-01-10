import './globals.css'

export const metadata = {
  title: 'Chess Application',
  description: 'Basic Chess Application',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
