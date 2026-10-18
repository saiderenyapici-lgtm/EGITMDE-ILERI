import zipfile
import os

files_data = {
    "frontend/src/components/AppShell.jsx": '''import { NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "@/lib/auth";
import { ThemeToggle } from "@/components/ThemeToggle";
import { Home, Sparkles, MessagesSquare, User as UserIcon, LogOut, GraduationCap } from "lucide-react";
import { Button } from "@/components/ui/button";

export function AppShell({ children }) {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const nav = [
    { to: "/feed", label: "Akış", icon: Home, testid: "nav-feed" },
    { to: "/ai", label: "Zeki AI", icon: Sparkles, testid: "nav-ai" },
    { to: "/groups", label: "Odalar", icon: MessagesSquare, testid: "nav-groups" },
    { to: "/profile", label: "Profil", icon: UserIcon, testid: "nav-profile" },
  ];

  return (
    <div className="min-h-screen bg-background">
      {/* Top Header */}
      <header className="sticky top-0 z-30 backdrop-blur-xl bg-background/70 border-b border-border">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
          <button
            data-testid="brand-logo"
            onClick={() => navigate("/feed")}
            className="flex items-center gap-2 group"
          >
            <div className="h-9 w-9 rounded-2xl bg-orange-500 grid place-items-center shadow-lg shadow-orange-500/30 group-hover:rotate-6 transition-transform">
              <GraduationCap className="h-5 w-5 text-white" strokeWidth={2.5} />
            </div>
            <span className="font-extrabold tracking-tight text-lg">Ögrenci<span className="text-orange-500">+</span></span>
          </button>

          <nav className="hidden md:flex items-center gap-1">
            {nav.map((n) => (
              <NavLink
                key={n.to}
                to={n.to}
                data-testid={n.testid}
                className={({ isActive }) =>
                  `px-4 py-2 rounded-full text-sm font-semibold flex items-center gap-2 transition-all ${
                    isActive
                      ? "bg-orange-500 text-white shadow-md shadow-orange-500/30"
                      : "text-foreground/70 hover:text-foreground hover:bg-accent"
                  }`
                }
              >
                <n.icon className="h-4 w-4" strokeWidth={2.5} /> {n.label}
              </NavLink>
            ))}
          </nav>

          <div className="flex items-center gap-2">
            <ThemeToggle small />
            {user && (
              <Button
                data-testid="logout-btn"
                variant="ghost"
                size="icon"
                onClick={async () => {
                  await logout();
                  navigate("/login");
                }}
                className="rounded-full h-9 w-9"
                title="Çıkış"
              >
                <LogOut className="h-4 w-4" />
              </Button>
            )}
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 sm:px-6 py-6 pb-24 md:pb-8">{children}</main>

      {/* Mobile bottom tab */}
      <nav className="md:hidden fixed bottom-4 left-4 right-4 z-30 backdrop-blur-xl bg-card/90 border border-border rounded-full shadow-2xl shadow-black/10 px-2 py-2 flex items-center justify-around">
        {nav.map((n) => (
          <NavLink
            key={n.to}
            to={n.to}
            data-testid={`${n.testid}-mobile`}
            className={({ isActive }) =>
              `flex flex-col items-center gap-0.5 px-3 py-1.5 rounded-full text-[11px] font-semibold ${
                isActive ? "bg-orange-500 text-white" : "text-foreground/70"
              }`
            }
          >
            <n.icon className="h-5 w-5" strokeWidth={2.5} />
            {n.label}
          </NavLink>
        ))}
      </nav>
    </div>
  );
}''',

    "frontend/src/pages/Register.jsx": '''import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "@/lib/auth";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card } from "@/components/ui/card";
import { toast } from "sonner";
import { ThemeToggle } from "@/components/ThemeToggle";
import { GraduationCap } from "lucide-react";
import { LEVELS } from "@/lib/levels";

export default function Register() {
  const navigate = useNavigate();
  const { register } = useAuth();
  const [form, setForm] = useState({ name: "", email: "", password: "", school_level: "lise" });
  const [busy, setBusy] = useState(false);

  const upd = (k, v) => setForm((s) => ({ ...s, [k]: v }));

  const onSubmit = async (e) => {
    e.preventDefault();
    if (form.password.length < 6) {
      toast.error("Şifre en az 6 karakter olmalı");
      return;
    }
    setBusy(true);
    try {
      await register(form);
      toast.success("Hesabın oluşturuldu! Hoş geldin 🎉");
      navigate("/feed");
    } catch (err) {
      toast.error(err?.response?.data?.detail || "Kayıt başarısız");
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-6 grain-bg bg-gradient-to-br from-orange-50 via-stone-50 to-amber-50 dark:from-zinc-950 dark:via-zinc-950 dark:to-black">
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute -top-20 -left-20 h-96 w-96 rounded-full bg-emerald-400/20 blur-3xl animate-blob" />
        <div className="absolute bottom-10 right-10 h-80 w-80 rounded-full bg-orange-400/30 blur-3xl animate-blob" style={{ animationDelay: "4s" }} />
      </div>
      <div className="absolute top-5 right-5 z-10"><ThemeToggle small /></div>

      <Card className="relative z-10 w-full max-w-md p-8 rounded-3xl border-border/50 shadow-2xl shadow-black/5 bg-card/80 backdrop-blur-xl">
        <div className="flex items-center gap-2 mb-6">
          <div className="h-10 w-10 rounded-2xl bg-orange-500 grid place-items-center">
            <GraduationCap className="h-6 w-6 text-white" strokeWidth={2.5} />
          </div>
          <span className="font-extrabold text-xl">Öğrenci<span className="text-orange-500">+</span></span>
        </div>
        <h2 className="text-3xl font-bold mb-1">Aramıza katıl</h2>
        <p className="text-muted-foreground mb-6">Ücretsiz hesap oluştur, Zeki ile hemen çalışmaya başla.</p>

        <form onSubmit={onSubmit} className="space-y-4">
          <div className="space-y-1.5">
            <Label htmlFor="name">Ad Soyad</Label>
            <Input data-testid="name-input" id="name" value={form.name} onChange={(e)=>upd("name", e.target.value)} required placeholder="Ör. Zeynep Kaya" className="h-12 rounded-2xl" />
          </div>
          <div className="space-y-1.5">
            <Label htmlFor="email">E-posta</Label>
            <Input data-testid="email-input" id="email" type="email" value={form.email} onChange={(e)=>upd("email", e.target.value)} required placeholder="sen@okul.com" className="h-12 rounded-2xl" />
          </div>
          <div className="space-y-1.5">
            <Label htmlFor="password">Şifre</Label>
            <Input data-testid="password-input" id="password" type="password" value={form.password} onChange={(e)=>upd("password", e.target.value)} required placeholder="En az 6 karakter" className="h-12 rounded-2xl" />
          </div>
          <div className="space-y-2">
            <Label>Okul Seviyesi</Label>
            <div className="grid grid-cols-3 gap-2">
              {Object.entries(LEVELS).map(([key, l]) => (
                <button
                  type="button"
                  key={key}
                  data-testid={`level-select-${key}`}
                  onClick={() => upd("school_level", key)}
                  className={`p-3 rounded-2xl border-2 text-sm font-semibold transition-all ${
                    form.school_level === key
                      ? `${l.ring} ring-4 ring-offset-2 ring-offset-background border-transparent${l.text} bg-card`
                      : "border-border hover:border-foreground/30 text-foreground/70"
                  }`}
                >
                  <div className="text-xl mb-0.5">{l.emoji}</div>
                  {l.label}
                </button>
              ))}
            </div>
          </div>

          <Button data-testid="register-submit-btn" type="submit" disabled={busy} className="w-full h-12 rounded-full font-bold text-base bg-orange-500 hover:bg-orange-600 text-white shadow-lg shadow-orange-500/30">
            {busy ? "Hesap oluşturuluyor..." : "Hesap oluştur"}
          </Button>
        </form>

        <p className="text-sm text-muted-foreground text-center mt-6">
          Zaten hesabın var mı? <Link data-testid="login-link" to="/login" className="text-orange-500 font-semibold hover:underline">Giriş yap</Link>
        </p>
      </Card>
    </div>
  );
}''',

    "frontend/src/pages/Login.jsx": '''import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "@/lib/auth";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card } from "@/components/ui/card";
import { toast } from "sonner";
import { ThemeToggle } from "@/components/ThemeToggle";
import { Sparkles, GraduationCap, Users } from "lucide-react";

export default function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [email, setEmail] = useState("demo@ogrenci.app");
  const [password, setPassword] = useState("Demo1234!");
  const [busy, setBusy] = useState(false);

  const onSubmit = async (e) => {
    e.preventDefault();
    setBusy(true);
    try {
      await login({ email, password });
      toast.success("Hoş geldin!");
      navigate("/feed");
    } catch (err) {
      toast.error(err?.response?.data?.detail || "Giriş başarısız");
    } finally {
      setBusy(false);
    }
  };

  const googleLogin = () => {
    const redirectUrl = window.location.origin + "/feed";
    window.location.href = `https://auth.emergentagent.com/?redirect=${encodeURIComponent(redirectUrl)}`;
  };

  return (
    <div className="min-h-screen flex grain-bg bg-gradient-to-br from-orange-50 via-stone-50 to-amber-50 dark:from-zinc-950 dark:via-zinc-950 dark:to-black">
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute -top-20 -left-20 h-96 w-96 rounded-full bg-orange-400/30 blur-3xl animate-blob" />
        <div className="absolute top-40 -right-20 h-96 w-96 rounded-full bg-sky-400/20 blur-3xl animate-blob" style={{ animationDelay: "3s" }} />
        <div className="absolute bottom-0 left-1/3 h-80 w-80 rounded-full bg-emerald-400/20 blur-3xl animate-blob" style={{ animationDelay: "6s" }} />
      </div>

      <div className="absolute top-5 right-5 z-10"><ThemeToggle small /></div>

      <div className="hidden lg:flex relative z-10 w-1/2 p-14 flex-col justify-between">
        <div className="flex items-center gap-3">
          <div className="h-12 w-12 rounded-2xl bg-orange-500 grid place-items-center shadow-xl shadow-orange-500/40">
            <GraduationCap className="h-7 w-7 text-white" strokeWidth={2.5} />
          </div>
          <span className="font-extrabold text-2xl">Öğrenci<span className="text-orange-500">+</span></span>
        </div>
        <div className="space-y-6">
          <h1 className="text-5xl font-extrabold tracking-tight leading-[1.05]">
            Öğren, paylaş, <br />
            <span className="text-orange-500">birlikte yüksel.</span>
          </h1>
          <p className="text-lg text-muted-foreground max-w-md">
            Türkiye'nin öğrenci topluluğu. Yapay zeka asistanın <b>Zeki</b> ile ders çalış, ilkokul-ortaokul-lise odalarında sohbet et.
          </p>
          <div className="flex flex-wrap gap-3">
            <div className="flex items-center gap-2 bg-card/60 backdrop-blur border border-border rounded-full px-4 py-2 text-sm">
              <Sparkles className="h-4 w-4 text-orange-500" /> AI ödev yardımı
            </div>
            <div className="flex items-center gap-2 bg-card/60 backdrop-blur border border-border rounded-full px-4 py-2 text-sm">
              <Users className="h-4 w-4 text-emerald-500" /> Okul odaları
            </div>
          </div>
        </div>
        <div className="text-xs text-muted-foreground">© 2026 Öğrenci+ · Türk öğrenciler için ❤️</div>
      </div>

      <div className="relative z-10 w-full lg:w-1/2 flex items-center justify-center p-6">
        <Card className="w-full max-w-md p-8 rounded-3xl border-border/50 shadow-2xl shadow-black/5 bg-card/80 backdrop-blur-xl">
          <div className="flex lg:hidden items-center justify-center gap-2 mb-6">
            <div className="h-10 w-10 rounded-2xl bg-orange-500 grid place-items-center">
              <GraduationCap className="h-6 w-6 text-white" strokeWidth={2.5} />
            </div>
            <span className="font-extrabold text-xl">Öğrenci<span className="text-orange-500">+</span></span>
          </div>
          <h2 className="text-3xl font-bold mb-1">Tekrar hoş geldin!</h2>
          <p className="text-muted-foreground mb-6">Çalışmaya kaldığın yerden devam et.</p>

          <Button
            data-testid="google-login-btn"
            type="button"
            variant="outline"
            onClick={googleLogin}
            className="w-full h-12 rounded-full font-semibold mb-5 border-2 hover:bg-accent"
          >
            <svg className="h-5 w-5 mr-2" viewBox="0 0 24 24">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
              <path fill="#FBBC05" d="M5.84 14.1A6.998 6.998 0 015.46 12c0-.73.13-1.44.36-2.1V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.83z"/>
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.07.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.83C6.71 7.31 9.14 5.38 12 5.38z"/>
            </svg>
            Google ile giriş yap
          </Button>

          <div className="relative my-5">
            <div className="absolute inset-0 flex items-center"><span className="w-full border-t border-border" /></div>
            <div className="relative flex justify-center text-xs uppercase tracking-wider">
              <span className="bg-card px-3 text-muted-foreground">veya</span>
            </div>
          </div>

          <form onSubmit={onSubmit} className="space-y-4">
            <div className="space-y-1.5">
              <Label htmlFor="email">E-posta</Label>
              <Input data-testid="email-input" id="email" type="email" value={email} onChange={(e)=>setEmail(e.target.value)} required placeholder="ornek@okul.com" className="h-12 rounded-2xl" />
            </div>
            <div className="space-y-1.5">
              <Label htmlFor="password">Şifre</Label>
              <Input data-testid="password-input" id="password" type="password" value={password} onChange={(e)=>setPassword(e.target.value)} required placeholder="••••••••" className="h-12 rounded-2xl" />
            </div>
            <Button data-testid="login-submit-btn" type="submit" disabled={busy} className="w-full h-12 rounded-full font-bold text-base bg-orange-500 hover:bg-orange-600 text-white shadow-lg shadow-orange-500/30 transition-all hover:scale-[1.01] active:scale-[0.98]">
              {busy ? "Giriş yapılıyor..." : "Giriş yap"}
            </Button>
          </form>

          <p className="text-sm text-muted-foreground text-center mt-6">
            Hesabın yok mu? <Link data-testid="register-link" to="/register" className="text-orange-500 font-semibold hover:underline">Kayıt ol</Link>
          </p>
        </Card>
      </div>
    </div>
  );
}''',

    "frontend/src/pages/AuthCallback.jsx": '''import { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { authApi } from "@/lib/apiClient";
import { useAuth } from "@/lib/auth";
import { GraduationCap } from "lucide-react";

export default function AuthCallback() {
  const navigate = useNavigate();
  const { setUser } = useAuth();
  const [error, setError] = useState("");
  const processed = useRef(false);

  useEffect(() => {
    if (processed.current) return;
    processed.current = true;

    const hash = window.location.hash || "";
    const match = hash.match(/session_id=([^&]+)/);
    if (!match) {
      navigate("/login");
      return;
    }
    const session_id = decodeURIComponent(match[1]);

    (async () => {
      try {
        const res = await authApi.googleSession(session_id);
        setUser(res.user);
        window.history.replaceState({}, "", "/feed");
        navigate("/feed", { state: { user: res.user } });
      } catch (e) {
        setError("Google ile giriş başarısız oldu. Lütfen tekrar deneyin.");
        setTimeout(() => navigate("/login"), 2000);
      }
    })();
  }, [navigate, setUser]);

  return (
    <div className="min-h-screen grid place-items-center bg-background">
      <div className="text-center">
        <div className="h-14 w-14 rounded-2xl bg-orange-500 grid place-items-center mx-auto mb-4 animate-pulse">
          <GraduationCap className="h-8 w-8 text-white" />
        </div>
        <p className="text-lg font-semibold">Giriş yapılıyor...</p>
        {error && <p className="text-destructive mt-2">{error}</p>}
      </div>
    </div>
  );
}''',

    "frontend/src/pages/Groups.jsx": '''import { Link } from "react-router-dom";
import { LEVELS } from "@/lib/levels";
import { Card } from "@/components/ui/card";
import { ArrowRight, Users } from "lucide-react";

export default function Groups() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight">Okul Odaları</h1>
        <p className="text-muted-foreground mt-1">Seviyene uygun odaya katıl, soru sor, arkadaş edin.</p>
      </div>

      <div className="grid md:grid-cols-3 gap-5">
        {Object.entries(LEVELS).map(([key, l]) => (
          <Link
            key={key}
            to={`/groups/${key}`}
            data-testid={`groups-card-${key}`}
            className="group"
          >
            <Card className={`relative overflow-hidden rounded-3xl p-6 bg-gradient-to-br ${l.bg} border-0 h-56 flex flex-col justify-between transition-all duration-300 group-hover:-translate-y-1 group-hover:shadow-2xl`}>
              <div className="relative z-10">
                <div className="inline-flex items-center gap-1.5 bg-black/10 dark:bg-white/10 backdrop-blur rounded-full px-3 py-1 text-xs font-semibold">
                  <Users className="h-3 w-3" /> Canlı
                </div>
                <h2 className="text-2xl font-extrabold mt-3">{l.label}</h2>
                <p className="text-sm opacity-80 mt-1">{l.label} öğrencileri için ortak oda.</p>
              </div>
              <div className="relative z-10 flex items-center justify-between">
                <span className="text-6xl">{l.emoji}</span>
                <div className="h-11 w-11 rounded-full bg-white/90 dark:bg-black/40 grid place-items-center backdrop-blur">
                  <ArrowRight className="h-5 w-5" strokeWidth={2.5} />
                </div>
              </div>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}''',

    "frontend/src/pages/AiChat.jsx": '''import { useEffect, useRef, useState } from "react";
import { aiApi, API } from "@/lib/apiClient";
import { useAuth } from "@/lib/auth";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Sparkles, Send, Plus, BookOpen, CalendarCheck, FileText, GraduationCap } from "lucide-react";
import { toast } from "sonner";

const MODES = {
  chat: { label: "Ders Yardımı", icon: BookOpen, hint: "Herhangi bir soruyu sor, adım adım açıklayayım." },
  plan: { label: "Çalışma Planı", icon: CalendarCheck, hint: "Dersini, sınav tarihini ve müsait saatlerini yaz." },
  summary: { label: "Özet Çıkar", icon: FileText, hint: "Özetlenmesini istediğin metni yapıştır." },
};

export default function AiChat() {
  const { user } = useAuth();
  const [sessions, setSessions] = useState([]);
  const [activeId, setActiveId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [mode, setMode] = useState("chat");
  const [streaming, setStreaming] = useState(false);
  const [streamText, setStreamText] = useState("");
  const scrollRef = useRef(null);

  const loadSessions = async () => {
    try {
      const s = await aiApi.sessions();
      setSessions(s);
      if (!activeId && s.length) {
        setActiveId(s[0].session_id);
      } else if (!s.length) {
        const ns = await aiApi.createSession();
        setSessions([ns]);
        setActiveId(ns.session_id);
      }
    } catch { toast.error("AI oturumları yüklenemedi"); }
  };

  const loadMessages = async (sid) => {
    try {
      const m = await aiApi.messages(sid);
      setMessages(m);
      setTimeout(() => scrollRef.current?.scrollTo({ top: 99999, behavior: "smooth" }), 60);
    } catch {}
  };

  useEffect(() => { loadSessions(); }, []);
  useEffect(() => { if (activeId) loadMessages(activeId); }, [activeId]);

  const newChat = async () => {
    try {
      const ns = await aiApi.createSession();
      setSessions((s) => [ns, ...s]);
      setActiveId(ns.session_id);
      setMessages([]);
    } catch { toast.error("Yeni sohbet açılamadı"); }
  };

  const send = async () => {
    const text = input.trim();
    if (!text || streaming || !activeId) return;
    setInput("");
    setMessages((ms) => [...ms, { role: "user", content: text, created_at: new Date().toISOString() }]);
    setStreaming(true);
    setStreamText("");
    setTimeout(() => scrollRef.current?.scrollTo({ top: 99999 }), 20);

    try {
      const res = await fetch(`${API}/ai/chat`, {
        method: "POST",
        credentials: "include",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: activeId, text, mode }),
      });
      if (!res.ok || !res.body) throw new Error("Stream başlatılamadı");
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let full = "";
      let buffer = "";
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const parts = buffer.split("\\n\\n");
        buffer = parts.pop();
        for (const chunk of parts) {
          if (!chunk.startsWith("data: ")) continue;
          const payload = chunk.slice(6);
          if (payload === "[DONE]") continue;
          full += payload.replace(/\\\\n/g, "\\n");
          setStreamText(full);
          scrollRef.current?.scrollTo({ top: 99999 });
        }
      }
      setMessages((ms) => [...ms, { role: "assistant", content: full, created_at: new Date().toISOString() }]);
      setStreamText("");
      loadSessions();
    } catch {
      toast.error("Zeki şu an cevap veremedi. Tekrar deneyin.");
    } finally {
      setStreaming(false);
    }
  };

  const quickSuggest = {
    chat: ["x² - 5x + 6 = 0 denklemini çöz", "Osmanlı duraklama nedenleri?", "İngilizce present perfect kullanımı"],
    plan: ["Pazartesi TYT denemem var, 3 gün planı çıkar", "Günde 2 saat matematik planı", "Haftalık fen bilimleri programı"],
    summary: ["Metni yapıştır, 5 maddede özetle", "Konuyu kısaca anlat", "Önemli terimleri çıkar"],
  };

  return (
    <div className="grid lg:grid-cols-12 gap-5">
      <aside className="lg:col-span-3 space-y-3">
        <Button data-testid="new-ai-chat-btn" onClick={newChat} className="w-full rounded-2xl bg-orange-500 hover:bg-orange-600 text-white font-semibold h-11">
          <Plus className="h-4 w-4 mr-1.5" /> Yeni Sohbet
        </Button>
        <Card className="rounded-3xl p-3 max-h-[65vh] overflow-y-auto scroll-soft">
          <div className="text-xs font-bold uppercase tracking-wider text-muted-foreground px-2 mb-2">Geçmiş</div>
          {sessions.length === 0 && <div className="text-sm text-muted-foreground p-3">Henüz sohbet yok.</div>}
          {sessions.map((s) => (
            <button
              key={s.session_id}
              data-testid={`ai-session-${s.session_id}`}
              onClick={() => setActiveId(s.session_id)}
              className={`w-full text-left px-3 py-2.5 rounded-2xl text-sm transition-colors ${activeId === s.session_id ? "bg-orange-500/10 text-orange-600 dark:text-orange-400 font-semibold" : "hover:bg-accent"}`}
            >
              <div className="truncate">{s.title || "Yeni Sohbet"}</div>
            </button>
          ))}
        </Card>
      </aside>

      <section className="lg:col-span-9">
        <Card className="rounded-3xl overflow-hidden flex flex-col" style={{ height: "78vh" }}>
          <div className="px-5 py-4 border-b border-border flex items-center justify-between bg-gradient-to-r from-orange-500/10 via-rose-500/5 to-orange-500/10">
            <div className="flex items-center gap-3">
              <div className="h-11 w-11 rounded-2xl bg-orange-500 grid place-items-center shadow-lg shadow-orange-500/30">
                <Sparkles className="h-5 w-5 text-white" strokeWidth={2.5} />
              </div>
              <div>
                <div className="font-bold">Zeki AI</div>
                <div className="text-xs text-muted-foreground">Gemini 3 Flash · Türkçe öğretmen asistanı</div>
              </div>
            </div>
            <div className="flex gap-1 bg-muted/60 p-1 rounded-full">
              {Object.entries(MODES).map(([k, m]) => (
                <button
                  key={k}
                  data-testid={`mode-${k}`}
                  onClick={() => setMode(k)}
                  className={`px-3 py-1.5 rounded-full text-xs font-semibold flex items-center gap-1.5 transition-all ${mode === k ? "bg-background shadow-sm" : "text-muted-foreground"}`}
                >
                  <m.icon className="h-3.5 w-3.5" /> <span className="hidden sm:inline">{m.label}</span>
                </button>
              ))}
            </div>
          </div>

          <div ref={scrollRef} className="flex-1 overflow-y-auto scroll-soft p-5 space-y-4">
            {messages.length === 0 && !streaming && (
              <div className="h-full flex flex-col items-center justify-center text-center space-y-4">
                <div className="h-20 w-20 rounded-3xl bg-orange-500 grid place-items-center shadow-2xl shadow-orange-500/40">
                  <GraduationCap className="h-10 w-10 text-white" strokeWidth={2.5} />
                </div>
                <div>
                  <div className="text-2xl font-extrabold tracking-tight">Merhaba, ben Zeki 👋</div>
                  <div className="text-muted-foreground mt-1">{MODES[mode].hint}</div>
                </div>
                <div className="flex flex-wrap gap-2 justify-center max-w-xl">
                  {quickSuggest[mode].map((s) => (
                    <button
                      key={s}
                      data-testid={`suggest-${s.slice(0,10)}`}
                      onClick={() => setInput(s)}
                      className="px-4 py-2 rounded-full border border-border hover:border-orange-500 hover:text-orange-500 text-sm transition-colors"
                    >
                      {s}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {messages.map((m, i) => (
              <div key={i} className={`flex gap-3 ${m.role === "user" ? "flex-row-reverse" : ""} animate-fade-up`}>
                {m.role === "assistant" ? (
                  <div className="h-9 w-9 rounded-2xl bg-orange-500 grid place-items-center shrink-0">
                    <Sparkles className="h-4 w-4 text-white" />
                  </div>
                ) : (
                  <Avatar className="h-9 w-9 shrink-0">
                    <AvatarImage src={user?.picture} />
                    <AvatarFallback>{user?.name?.slice(0,1)}</AvatarFallback>
                  </Avatar>
                )}
                <div className={`max-w-[75%] px-4 py-3 rounded-2xl ${m.role === "user" ? "bg-orange-500 text-white rounded-br-sm" : "bg-muted rounded-bl-sm"}`}>
                  <div className="whitespace-pre-wrap leading-relaxed">{m.content}</div>
                </div>
              </div>
            ))}

            {streaming && (
              <div className="flex gap-3 animate-fade-up">
                <div className="h-9 w-9 rounded-2xl bg-orange-500 grid place-items-center shrink-0">
                  <Sparkles className="h-4 w-4 text-white" />
                </div>
                <div className="max-w-[75%] px-4 py-3 rounded-2xl bg-muted rounded-bl-sm">
                  {streamText ? (
                    <div className="whitespace-pre-wrap leading-relaxed">{streamText}<span className="inline-block ml-0.5 w-1.5 h-4 bg-orange-500 align-middle animate-pulse" /></div>
                  ) : (
                    <div className="flex gap-1">
                      <span className="w-2 h-2 rounded-full bg-orange-500 typing-dot" />
                      <span className="w-2 h-2 rounded-full bg-orange-500 typing-dot" style={{ animationDelay: "0.2s" }} />
                      <span className="w-2 h-2 rounded-full bg-orange-500 typing-dot" style={{ animationDelay: "0.4s" }} />
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>

          <div className="p-4 border-t border-border bg-card">
            <div className="flex gap-2">
              <textarea
                data-testid="ai-input"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(); } }}
                placeholder={MODES[mode].hint}
                rows={1}
                className="flex-1 px-5 py-3 rounded-3xl bg-muted/60 border border-border focus:outline-none focus:ring-2 focus:ring-orange-500/40 resize-none max-h-32"
              />
              <Button data-testid="ai-send-btn" onClick={send} disabled={streaming || !input.trim()} className="rounded-full h-12 w-12 bg-orange-500 hover:bg-orange-600 p-0">
                <Send className="h-5 w-5" />
              </Button>
            </div>
          </div>
        </Card>
      </section>
    </div>
  );
}''',

    "frontend/src/pages/Profile.jsx": '''import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { usersApi } from "@/lib/apiClient";
import { useAuth } from "@/lib/auth";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { LevelChip, LEVELS } from "@/lib/levels";
import { toast } from "sonner";
import { Mail, UserPlus, UserCheck, Calendar } from "lucide-react";

export default function Profile() {
  const { id } = useParams();
  const { user } = useAuth();
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const targetId = id || user?.user_id;
  const isMe = !id || id === user?.user_id;

  const load = async () => {
    if (!targetId) return;
    setLoading(true);
    try {
      const p = await usersApi.get(targetId);
      setProfile(p);
    } catch { toast.error("Profil yüklenemedi"); }
    finally { setLoading(false); }
  };
  useEffect(() => { load(); }, [targetId]);

  const onFollow = async () => {
    try {
      const r = await usersApi.follow(targetId);
      setProfile((p) => ({ ...p, is_following: r.following, followers: (p?.followers || 0) + (r.following ? 1 : -1) }));
      toast.success(r.following ? "Takip edildi" : "Takipten çıkıldı");
    } catch { toast.error("İşlem başarısız"); }
  };

  if (loading || !profile) return <div className="text-center py-20 text-muted-foreground">Yükleniyor...</div>;
  const L = LEVELS[profile.school_level] || LEVELS.lise;

  return (
    <div className="max-w-3xl mx-auto">
      <div className={`relative overflow-hidden rounded-3xl h-40 bg-gradient-to-br ${L.bg}`}>
        <div className="absolute -right-6 -bottom-6 text-9xl opacity-30">{L.emoji}</div>
      </div>

      <div className="px-6 -mt-14 relative">
        <Avatar className="h-28 w-28 ring-4 ring-background">
          <AvatarImage src={profile.picture} />
          <AvatarFallback className="text-3xl">{profile.name?.slice(0,1)}</AvatarFallback>
        </Avatar>
        <div className="flex items-start justify-between flex-wrap gap-3 mt-4">
          <div>
            <div className="flex items-center gap-2 flex-wrap">
              <h1 className="text-3xl font-extrabold tracking-tight">{profile.name}</h1>
              <LevelChip level={profile.school_level} />
            </div>
            <div className="flex items-center gap-3 text-sm text-muted-foreground mt-1">
              <span className="flex items-center gap-1"><Mail className="h-3.5 w-3.5" /> {profile.email}</span>
            </div>
            {profile.bio && <p className="mt-3 max-w-xl">{profile.bio}</p>}
          </div>

          {!isMe && (
            <Button
              data-testid="follow-btn"
              onClick={onFollow}
              className={`rounded-full font-semibold px-6 ${profile.is_following ? "bg-muted text-foreground hover:bg-muted/80" : "bg-orange-500 hover:bg-orange-600 text-white"}`}
            >
              {profile.is_following ? <><UserCheck className="h-4 w-4 mr-1.5" /> Takiptesin</> : <><UserPlus className="h-4 w-4 mr-1.5" /> Takip et</>}
            </Button>
          )}
        </div>

        <div className="grid grid-cols-3 gap-3 mt-6">
          <Card className="rounded-3xl p-4 text-center">
            <div className="text-2xl font-extrabold">{profile.followers || 0}</div>
            <div className="text-xs text-muted-foreground mt-0.5">Takipçi</div>
          </Card>
          <Card className="rounded-3xl p-4 text-center">
            <div className="text-2xl font-extrabold">{profile.following || 0}</div>
            <div className="text-xs text-muted-foreground mt-0.5">Takip</div>
          </Card>
          <Card className="rounded-3xl p-4 text-center">
            <div className="text-2xl font-extrabold">{L.emoji}</div>
            <div className="text-xs text-muted-foreground mt-0.5">{L.label}</div>
          </Card>
        </div>

        <Card className="rounded-3xl p-6 mt-5">
          <h3 className="font-bold mb-2">Hakkında</h3>
          <div className="text-sm text-muted-foreground flex items-center gap-2">
            <Calendar className="h-4 w-4" /> Katılım: {profile.created_at?.slice(0,10)}
          </div>
        </Card>
      </div>
    </div>
  );
}''',

    "frontend/src/App.js": '''import "@/App.css";
import { BrowserRouter, Routes, Route, Navigate, useLocation } from "react-router-dom";
import { AuthProvider, useAuth } from "@/lib/auth";
import { Toaster } from "@/components/ui/sonner";

import Login from "@/pages/Login";
import Register from "@/pages/Register";
import AuthCallback from "@/pages/AuthCallback";
import Feed from "@/pages/Feed";
import Groups from "@/pages/Groups";
import GroupChat from "@/pages/GroupChat";
import AiChat from "@/pages/AiChat";
import Profile from "@/pages/Profile";
import { AppShell } from "@/components/AppShell";

function Protected({ children }) {
  const { user, loading } = useAuth();
  if (loading) {
    return (
      <div className="min-h-screen grid place-items-center">
        <div className="h-10 w-10 rounded-full border-4 border-orange-500/20 border-t-orange-500 animate-spin" />
      </div>
    );
  }
  if (!user) return <Navigate to="/login" replace />;
  return <AppShell>{children}</AppShell>;
}

function AppRouter() {
  const location = useLocation();
  if (location.hash?.includes("session_id=")) {
    return <AuthCallback />;
  }
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/feed" element={<Protected><Feed /></Protected>} />
      <Route path="/ai" element={<Protected><AiChat /></Protected>} />
      <Route path="/groups" element={<Protected><Groups /></Protected>} />
      <Route path="/groups/:level" element={<Protected><GroupChat /></Protected>} />
      <Route path="/profile" element={<Protected><Profile /></Protected>} />
      <Route path="/profile/:id" element={<Protected><Profile /></Protected>} />
      <Route path="/" element={<Navigate to="/feed" replace />} />
      <Route path="*" element={<Navigate to="/feed" replace />} />
    </Routes>
  );
}

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <AuthProvider>
          <AppRouter />
          <Toaster richColors position="top-center" />
        </AuthProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
'''
}

os.makedirs('ogrenci_plus_project', exist_ok=True)
for path, content in files_data.items():
    full_path = os.path.join('ogrenci_plus_project', path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

zip_filename = 'ogrenci_plus_project.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk('ogrenci_plus_project'):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, 'ogrenci_plus_project')
            zipf.write(file_path, arcname)

print("Zip created successfully:", zip_filename)
