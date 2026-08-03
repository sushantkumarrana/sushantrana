"use client";

import { Canvas, useFrame } from "@react-three/fiber";
import { Float, MeshDistortMaterial, Sparkles } from "@react-three/drei";
import { useRef, useMemo } from "react";
import type { Mesh, Group } from "three";

function Knot({ reduced }: { reduced: boolean }) {
  const mesh = useRef<Mesh>(null);
  const group = useRef<Group>(null);

  useFrame((state, delta) => {
    if (mesh.current) {
      mesh.current.rotation.y += delta * (reduced ? 0.05 : 0.25);
      mesh.current.rotation.x += delta * (reduced ? 0.02 : 0.08);
    }
    if (group.current && !reduced) {
      // ease the whole group toward the pointer for a parallax/tilt feel
      const { x, y } = state.pointer;
      group.current.rotation.y += (x * 0.5 - group.current.rotation.y) * 0.05;
      group.current.rotation.x += (-y * 0.4 - group.current.rotation.x) * 0.05;
    }
  });

  return (
    <group ref={group}>
      <Float speed={reduced ? 0 : 1.4} rotationIntensity={0.4} floatIntensity={0.9}>
        <mesh ref={mesh} scale={2.15}>
          <icosahedronGeometry args={[1, 12]} />
          <MeshDistortMaterial
            color="#f97316"
            emissive="#7c2d12"
            emissiveIntensity={0.5}
            roughness={0.25}
            metalness={0.35}
            distort={reduced ? 0.15 : 0.4}
            speed={reduced ? 0 : 1.6}
          />
        </mesh>
      </Float>
      {!reduced && (
        <Sparkles count={60} scale={7} size={3} speed={0.4} color="#fdba74" />
      )}
    </group>
  );
}

export default function Hero3D() {
  const reduced = useMemo(
    () =>
      typeof window !== "undefined" &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches,
    []
  );

  return (
    <Canvas
      camera={{ position: [0, 0, 6], fov: 45 }}
      dpr={[1, 2]}
      gl={{ antialias: true, alpha: true }}
      style={{ background: "transparent" }}
    >
      <ambientLight intensity={0.35} />
      <pointLight position={[5, 5, 5]} intensity={120} color="#ffd7b0" />
      <pointLight position={[-6, -3, 2]} intensity={80} color="#ea580c" />
      <pointLight position={[0, 3, -5]} intensity={60} color="#f97316" />
      <Knot reduced={reduced} />
    </Canvas>
  );
}
