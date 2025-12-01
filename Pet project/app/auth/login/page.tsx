"use client";

import { useAuth } from "@/lib/auth/context";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
    const { login, isLoggedIn, loading } = useAuth();
    const router = useRouter();
    const [error, setError] = useState("");
    const [loadingState, setLoading] = useState(false);

    useEffect(() => {
        if (!loading && isLoggedIn) {
            router.replace("/protected");
        }
    }, [isLoggedIn, loading, router]);

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setLoading(true);
        setError("");

        const formData = new FormData(e.currentTarget);
        const username = formData.get("username") as string;
        const password = formData.get("password") as string;

        try {
            const response = await fetch("/api/users/auth/sign_in", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();

            if (response.ok) {
                login(username);
                router.push("/protected");
            } else {
                setError(data.error || "Login failed");
            }
        } catch (err) {
            setError("An unexpected error occurred");
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="min-h-screen flex items-center justify-center p-6">
            <div className="w-full max-w-sm">
                <h1 className="text-2xl font-semibold mb-4">Sign in</h1>
                {error && (
                    <div className="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
                        {error}
                    </div>
                )}
                <form onSubmit={handleSubmit} className="space-y-3">
                    <div className="flex flex-col gap-1">
                        <label htmlFor="username" className="text-sm">
                            Username
                        </label>
                        <input
                            id="username"
                            name="username"
                            type="text"
                            className="border rounded px-3 py-2"
                            required
                        />
                    </div>
                    <div className="flex flex-col gap-1">
                        <label htmlFor="password" className="text-sm">
                            Password
                        </label>
                        <input
                            id="password"
                            name="password"
                            type="password"
                            className="border rounded px-3 py-2"
                            required
                        />
                    </div>
                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full bg-black text-white rounded py-2 disabled:opacity-50"
                    >
                        {loading ? "Signing in..." : "Sign in"}
                    </button>
                </form>
                <p className="text-sm mt-3">
                    Don&apos;t have an account?{" "}
                    <a className="underline" href="/auth/sign-up">
                        Sign up
                    </a>
                </p>
            </div>
        </main>
    );
}
