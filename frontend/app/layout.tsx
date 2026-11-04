import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = { title: "DevPilot | AI Engineering Workspace", description: "Turn software ideas into reviewable engineering artifacts with AI agents." };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }
